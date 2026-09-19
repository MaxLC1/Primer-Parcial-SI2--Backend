from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.core.deps import get_current_user
from app.pkg_seguridad.models import Usuario
from . import schemas, services

router = APIRouter(tags=["Devoluciones"], prefix="/devoluciones")

@router.get("/", response_model=List[schemas.DevolucionOut])
def list_devoluciones(db: Session = Depends(get_db)):
    return services.get_devoluciones(db)

@router.post("/", response_model=schemas.DevolucionOut, status_code=status.HTTP_201_CREATED)
def create_devolucion(devolucion: schemas.DevolucionCreate, db: Session = Depends(get_db)):
    return services.create_devolucion(db, devolucion)

@router.put("/{dev_id}/estado", response_model=schemas.DevolucionOut)
def update_devolucion_estado(dev_id: int, payload: schemas.DevolucionUpdate, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    if current_user.rol.nombre != "Administrador":
        raise HTTPException(status_code=403, detail="No autorizado")
    return services.update_estado(db, dev_id, payload.estado)
