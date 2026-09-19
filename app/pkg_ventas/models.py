from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime

class Venta(Base):
    __tablename__ = "ventas"
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, default=datetime.utcnow)
    total = Column(Float, default=0.0)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    sucursal_id = Column(Integer, ForeignKey("sucursales.id"))
    metodo_pago = Column(String(50), default="Efectivo") # Efectivo, QR, Stripe
    transaccion_id = Column(String(100), nullable=True) # Para Stripe o QR id
    tipo_entrega = Column(String(50), default="Recojo en Tienda") # Delivery o Recojo en Tienda
    direccion_envio = Column(String(255), nullable=True)
    
    detalles = relationship("DetalleVenta", back_populates="venta")
    usuario = relationship("Usuario")
    sucursal = relationship("Sucursal")

class DetalleVenta(Base):
    __tablename__ = "detalle_ventas"
    id = Column(Integer, primary_key=True, index=True)
    venta_id = Column(Integer, ForeignKey("ventas.id"))
    producto_id = Column(Integer, ForeignKey("productos.id"))
    talla_id = Column(Integer, ForeignKey("tallas.id"))
    color_id = Column(Integer, ForeignKey("colores.id"))
    cantidad = Column(Integer, default=1)
    precio_unitario = Column(Float, nullable=False)
    subtotal = Column(Float, nullable=False)

    venta = relationship("Venta", back_populates="detalles")
    producto = relationship("Producto")
    talla = relationship("Talla")
    color = relationship("Color")
