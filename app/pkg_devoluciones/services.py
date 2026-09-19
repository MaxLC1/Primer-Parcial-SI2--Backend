from sqlalchemy.orm import Session
from . import models, schemas
from app.pkg_ventas.models import Venta
from fastapi import HTTPException

def get_devoluciones(db: Session):
    return db.query(models.Devolucion).all()

def create_devolucion(db: Session, devolucion: schemas.DevolucionCreate):
    # Verificar que la venta exista
    venta = db.query(Venta).filter(Venta.id == devolucion.venta_id).first()
    if not venta:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    
    db_devolucion = models.Devolucion(**devolucion.model_dump())
    db.add(db_devolucion)
    db.commit()
    db.refresh(db_devolucion)
    return db_devolucion

def update_estado(db: Session, dev_id: int, estado: str):
    dev = db.query(models.Devolucion).filter(models.Devolucion.id == dev_id).first()
    if not dev:
        raise HTTPException(status_code=404, detail="Devolución no encontrada")
    
    dev.estado = estado
    db.commit()
    db.refresh(dev)
    return dev
