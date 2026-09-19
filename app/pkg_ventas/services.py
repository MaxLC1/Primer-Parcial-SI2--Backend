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
        sucursal_id=venta.sucursal_id,
        metodo_pago=venta.metodo_pago,
        transaccion_id=venta.transaccion_id,
        tipo_entrega=venta.tipo_entrega,
        direccion_envio=venta.direccion_envio
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

    # Si es Delivery, crear la orden de servicio
    if venta.tipo_entrega == "Delivery":
        from app.pkg_delivery.models import ServicioDelivery
        db_delivery = ServicioDelivery(
            venta_id=db_venta.id,
            estado="Pendiente"
        )
        db.add(db_delivery)
        db.commit()

    return db_venta
    
def get_ventas(db: Session):
    return db.query(models.Venta).all()

def get_reportes(db: Session):
    from sqlalchemy.sql import func
    
    ventas = db.query(models.Venta).all()
    
    total_ingresos = sum(v.total for v in ventas) if ventas else 0
    total_ventas = len(ventas)
    ticket_promedio = total_ingresos / total_ventas if total_ventas > 0 else 0
    
    # KPIs simples para el dashboard
    return {
        "total_ingresos": total_ingresos,
        "total_ventas": total_ventas,
        "ticket_promedio": ticket_promedio,
        "ventas_por_metodo": {
            "Efectivo": len([v for v in ventas if v.metodo_pago == "Efectivo"]),
            "QR": len([v for v in ventas if v.metodo_pago == "QR"]),
            "Stripe": len([v for v in ventas if v.metodo_pago == "Stripe"]),
        }
    }
