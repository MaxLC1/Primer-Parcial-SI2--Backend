from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas
from app.pkg_sucursales.models import Inventario

def get_reservas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Reserva).offset(skip).limit(limit).all()

def create_reserva(db: Session, reserva: schemas.ReservaCreate):
    # Crear la reserva
    db_reserva = models.Reserva(
        usuario_id=reserva.usuario_id,
        sucursal_id=reserva.sucursal_id
    )
    db.add(db_reserva)
    db.commit()
    db.refresh(db_reserva)
    
    # Crear los detalles
    for detalle in reserva.detalles:
        db_detalle = models.DetalleReserva(
            reserva_id=db_reserva.id,
            producto_id=detalle.producto_id,
            talla_id=detalle.talla_id,
            color_id=detalle.color_id,
            cantidad=detalle.cantidad
        )
        db.add(db_detalle)
        
        # Opcional: Descontar inventario aquí
        # inventario = db.query(Inventario).filter_by(
        #     sucursal_id=reserva.sucursal_id,
        #     producto_id=detalle.producto_id,
        #     talla_id=detalle.talla_id,
        #     color_id=detalle.color_id
        # ).first()
        # if inventario and inventario.cantidad >= detalle.cantidad:
        #     inventario.cantidad -= detalle.cantidad
        # else:
        #     raise HTTPException(status_code=400, detail="Inventario insuficiente")

    db.commit()
    db.refresh(db_reserva)
    return db_reserva

def update_estado_reserva(db: Session, reserva_id: int, estado: str):
    db_reserva = db.query(models.Reserva).filter(models.Reserva.id == reserva_id).first()
    if not db_reserva:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    db_reserva.estado = estado
    db.commit()
    db.refresh(db_reserva)
    return db_reserva
