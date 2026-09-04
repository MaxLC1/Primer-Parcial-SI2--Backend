from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from typing import List

from app.core.database import get_db
from app.core import security
from . import schemas, services

router = APIRouter(tags=["Seguridad"])

@router.get("/usuarios", response_model=List[schemas.UsuarioOut])
def get_all_usuarios(db: Session = Depends(get_db)):
    """Obtiene la lista de todos los usuarios registrados."""
    return services.get_usuarios(db)

@router.post("/register", response_model=schemas.UsuarioOut, status_code=status.HTTP_201_CREATED)
def register(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    """Registra un nuevo usuario en la plataforma."""
    db_user = services.get_usuario_by_email(db, email=usuario.email)
    if db_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado.")
    
    return services.create_usuario(db=db, usuario=usuario)

@router.get("/roles", response_model=List[schemas.RolOut])
def read_roles(db: Session = Depends(get_db)):
    """Obtiene los roles del sistema."""
    return services.get_roles(db)

@router.post("/roles", response_model=schemas.RolOut, status_code=status.HTTP_201_CREATED)
def add_rol(rol: schemas.RolCreate, db: Session = Depends(get_db)):
    """Añade un nuevo rol (Admin, Vendedor, etc)."""
    return services.create_rol(db=db, rol=rol)

@router.post("/login", response_model=schemas.Token)
def login(usuario: schemas.UsuarioLogin, db: Session = Depends(get_db)):
    """Inicia sesión y devuelve un Token JWT."""
    user = services.authenticate_usuario(db, usuario.email, usuario.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Configurar expiración y crear token
    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.email, "id": user.id}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/change-password")
def change_password(data: schemas.ChangePasswordRequest, db: Session = Depends(get_db)):
    """Cambia la contraseña de un usuario."""
    user = services.update_password(db, data.user_id, data.new_password)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"message": "Contraseña actualizada exitosamente"}
