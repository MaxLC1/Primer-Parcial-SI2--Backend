from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from . import schemas, services

router = APIRouter(tags=["Catálogo"])

@router.get("/categorias", response_model=List[schemas.CategoriaOut])
def read_categorias(db: Session = Depends(get_db)):
    """Obtiene la lista de todas las categorías de ropa."""
    return services.get_categorias(db)

@router.post("/categorias", response_model=schemas.CategoriaOut, status_code=status.HTTP_201_CREATED)
def create_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    """Crea una nueva categoría."""
    return services.create_categoria(db=db, categoria=categoria)

@router.get("/productos", response_model=List[schemas.ProductoOut])
def read_productos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtiene el catálogo de productos con paginación."""
    return services.get_productos(db, skip=skip, limit=limit)

@router.post("/productos", response_model=schemas.ProductoOut, status_code=status.HTTP_201_CREATED)
def create_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    """Crea un nuevo producto en el catálogo."""
    return services.create_producto(db=db, producto=producto)

@router.get("/tallas", response_model=List[schemas.TallaOut])
def read_tallas(db: Session = Depends(get_db)):
    """Obtiene la lista de tallas de ropa."""
    return services.get_tallas(db)

@router.post("/tallas", response_model=schemas.TallaOut, status_code=status.HTTP_201_CREATED)
def create_talla(talla: schemas.TallaCreate, db: Session = Depends(get_db)):
    """Registra una nueva talla."""
    return services.create_talla(db=db, talla=talla)

@router.get("/colores", response_model=List[schemas.ColorOut])
def read_colores(db: Session = Depends(get_db)):
    """Obtiene la lista de colores registrados."""
    return services.get_colores(db)

@router.post("/colores", response_model=schemas.ColorOut, status_code=status.HTTP_201_CREATED)
def create_color(color: schemas.ColorCreate, db: Session = Depends(get_db)):
    """Registra un nuevo color (nombre y HEX)."""
    return services.create_color(db=db, color=color)
