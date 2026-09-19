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
    metodo_pago: str = "Efectivo"
    transaccion_id: Optional[str] = None
    tipo_entrega: str = "Recojo en Tienda"
    direccion_envio: Optional[str] = None
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
    metodo_pago: Optional[str] = None
    transaccion_id: Optional[str] = None
    tipo_entrega: Optional[str] = None
    direccion_envio: Optional[str] = None
    detalles: List[DetalleVentaOut]

    class Config:
        from_attributes = True
