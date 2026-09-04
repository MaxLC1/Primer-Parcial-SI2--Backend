from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas
from app.pkg_sucursales.models import Inventario

def create_venta(db: Session, venta: schemas.VentaCreate):
    # Calcular total y verificar inventario
    total_venta = 0.0
    
    for det in venta.detalles:
        # Verificar stock
        inv = db.query(Inventario).filter(
            Inventario.sucursal_id == venta.sucursal_id,
            Inventario.producto_id == det.producto_id,
            Inventario.talla_id == det.talla_id,
            Inventario.color_id == det.color_id
        ).first()
        
        if not inv or inv.cantidad < det.cantidad:
            raise HTTPException(status_code=400, detail=f"Stock insuficiente para producto ID {det.producto_id}")
            
        # Descontar inventario
        inv.cantidad -= det.cantidad
        
        # Sumar al total
        total_venta += det.cantidad * det.precio_unitario
        
    # Crear venta
    db_venta = models.Venta(
        total=total_venta,
        usuario_id=venta.usuario_id,
        sucursal_id=venta.sucursal_id
    )
    db.add(db_venta)
    db.commit()
    db.refresh(db_venta)
    
    # Crear detalles
    for det in venta.detalles:
        db_det = models.DetalleVenta(
            venta_id=db_venta.id,
            producto_id=det.producto_id,
            talla_id=det.talla_id,
            color_id=det.color_id,
            cantidad=det.cantidad,
            precio_unitario=det.precio_unitario,
            subtotal=det.cantidad * det.precio_unitario
        )
        db.add(db_det)
        
    db.commit()
    db.refresh(db_venta)
    return db_venta
    
def get_ventas(db: Session):
    return db.query(models.Venta).all()
