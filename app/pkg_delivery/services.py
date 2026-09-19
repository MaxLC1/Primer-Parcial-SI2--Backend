from sqlalchemy.orm import Session
from . import models, schemas
from app.pkg_devoluciones.models import Devolucion
from fastapi import HTTPException
from datetime import datetime

def get_entregas_by_repartidor(db: Session, repartidor_id: int):
    return db.query(models.ServicioDelivery).filter(models.ServicioDelivery.repartidor_id == repartidor_id).all()

def get_todas_entregas(db: Session):
    return db.query(models.ServicioDelivery).all()

def create_servicio(db: Session, delivery: schemas.DeliveryCreate):
    dev = db.query(Devolucion).filter(Devolucion.id == delivery.devolucion_id).first()
    if not dev:
        raise HTTPException(status_code=404, detail="Devolución no encontrada")
        
    db_delivery = models.ServicioDelivery(devolucion_id=delivery.devolucion_id)
    db.add(db_delivery)
    db.commit()
    db.refresh(db_delivery)
    return db_delivery

def assign_repartidor(db: Session, delivery_id: int, repartidor_id: int):
    delivery = db.query(models.ServicioDelivery).filter(models.ServicioDelivery.id == delivery_id).first()
    if not delivery:
        raise HTTPException(status_code=404, detail="Servicio de delivery no encontrado")
        
    delivery.repartidor_id = repartidor_id
    delivery.estado = "Asignado"
    delivery.fecha_asignacion = datetime.utcnow()
    db.commit()
    db.refresh(delivery)
    return delivery

def update_estado(db: Session, delivery_id: int, estado: str):
    delivery = db.query(models.ServicioDelivery).filter(models.ServicioDelivery.id == delivery_id).first()
    if not delivery:
        raise HTTPException(status_code=404, detail="Servicio de delivery no encontrado")
        
    delivery.estado = estado
    db.commit()
    db.refresh(delivery)
    return delivery
