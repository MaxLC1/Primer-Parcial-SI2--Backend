from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from . import schemas, services

router = APIRouter(tags=["Sucursales"])

@router.get("/ciudades", response_model=List[schemas.CiudadOut])
def read_ciudades(db: Session = Depends(get_db)):
    """Obtiene la lista de todas las ciudades."""
    return services.get_ciudades(db)

@router.post("/ciudades", response_model=schemas.CiudadOut, status_code=status.HTTP_201_CREATED)
def create_ciudad(ciudad: schemas.CiudadCreate, db: Session = Depends(get_db)):
    """Registra una nueva ciudad."""
    return services.create_ciudad(db=db, ciudad=ciudad)

@router.get("/sucursales", response_model=List[schemas.SucursalOut])
def read_sucursales(db: Session = Depends(get_db)):
    """Obtiene la lista de sucursales registradas."""
    return services.get_sucursales(db)

@router.post("/sucursales", response_model=schemas.SucursalOut, status_code=status.HTTP_201_CREATED)
def create_sucursal(sucursal: schemas.SucursalCreate, db: Session = Depends(get_db)):
    """Crea una nueva sucursal y la asocia a una ciudad."""
    return services.create_sucursal(db=db, sucursal=sucursal)

@router.put("/sucursales/{sucursal_id}", response_model=schemas.SucursalOut)
def update_sucursal(sucursal_id: int, data: schemas.SucursalUpdate, db: Session = Depends(get_db)):
    """Actualiza una sucursal existente."""
    from fastapi import HTTPException
    sucursal = services.update_sucursal(db, sucursal_id, data)
    if not sucursal:
        raise HTTPException(status_code=404, detail="Sucursal no encontrada.")
    return sucursal

@router.get("/inventarios", response_model=List[schemas.InventarioOut])
def read_inventarios(db: Session = Depends(get_db)):
    """Obtiene el inventario global de todas las sucursales."""
    return services.get_inventarios(db)

@router.post("/inventarios", response_model=schemas.InventarioOut, status_code=status.HTTP_201_CREATED)
def add_inventario(inventario: schemas.InventarioCreate, db: Session = Depends(get_db)):
    """Añade stock a una combinación específica."""
    return services.create_inventario(db=db, inventario=inventario)

@router.put("/inventarios/{inventario_id}", response_model=schemas.InventarioOut)
def update_inventario(inventario_id: int, data: schemas.InventarioUpdate, db: Session = Depends(get_db)):
    """Ajusta el stock de un registro de inventario."""
    from fastapi import HTTPException
    inv = services.update_inventario(db, inventario_id, data)
    if not inv:
        raise HTTPException(status_code=404, detail="Registro de inventario no encontrado.")
    return inv
