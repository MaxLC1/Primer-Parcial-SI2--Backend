from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class Devolucion(Base):
    __tablename__ = "devoluciones"

    id = Column(Integer, primary_key=True, index=True)
    venta_id = Column(Integer, ForeignKey("ventas.id"), nullable=False)
    motivo = Column(String(255), nullable=False)
    tipo_solicitud = Column(String(50), default="Devolución", nullable=False)
    requiere_delivery = Column(Integer, default=0, nullable=False) # Usamos Integer como boolean compatibility
    estado = Column(String(50), default="Pendiente") # Pendiente, Aprobada, Rechazada, Completada
    fecha_solicitud = Column(DateTime, default=datetime.utcnow)

    # Relaciones
    venta = relationship("Venta")
