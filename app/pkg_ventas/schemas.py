from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class DetalleVentaCreate(BaseModel):
    producto_id: int
    talla_id: int
    color_id: int
    cantidad: int
    precio_unitario: float

class VentaCreate(BaseModel):
    sucursal_id: int
    usuario_id: int
    detalles: List[DetalleVentaCreate]

class DetalleVentaOut(BaseModel):
    id: int
    producto_id: int
    talla_id: int
    color_id: int
    cantidad: int
    precio_unitario: float
    subtotal: float
    
    class Config:
        from_attributes = True

class VentaOut(BaseModel):
    id: int
    fecha: datetime
    total: float
    usuario_id: int
    sucursal_id: int
    detalles: List[DetalleVentaOut]

    class Config:
        from_attributes = True
