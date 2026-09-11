from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class DetalleReservaBase(BaseModel):
    producto_id: int
    talla_id: int
    color_id: int
    cantidad: int = 1

class DetalleReservaCreate(DetalleReservaBase):
    pass

class DetalleReservaOut(DetalleReservaBase):
    id: int
    reserva_id: int
    class Config:
        from_attributes = True

class ReservaBase(BaseModel):
    usuario_id: int
    sucursal_id: int

class ReservaCreate(ReservaBase):
    detalles: List[DetalleReservaCreate]

class ReservaOut(ReservaBase):
    id: int
    fecha_reserva: datetime
    estado: str
    detalles: List[DetalleReservaOut] = []
    
    class Config:
        from_attributes = True
