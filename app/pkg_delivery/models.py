from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class ServicioDelivery(Base):
    __tablename__ = "servicio_delivery"

    id = Column(Integer, primary_key=True, index=True)
    devolucion_id = Column(Integer, ForeignKey("devoluciones.id"), nullable=True)
    venta_id = Column(Integer, ForeignKey("ventas.id"), nullable=True)
    repartidor_id = Column(Integer, ForeignKey("usuarios.id"), nullable=True)
    estado = Column(String(50), default="Pendiente") # Pendiente, Asignado, En Camino, Recogido, Completado
    fecha_asignacion = Column(DateTime, nullable=True)

    # Relaciones
    devolucion = relationship("Devolucion")
    repartidor = relationship("Usuario")
