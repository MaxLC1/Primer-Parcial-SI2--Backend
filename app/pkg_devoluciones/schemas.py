from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DevolucionBase(BaseModel):
    venta_id: int
    motivo: str
    tipo_solicitud: str = "Devolución"
    requiere_delivery: int = 0

class DevolucionCreate(DevolucionBase):
    pass

class DevolucionOut(DevolucionBase):
    id: int
    estado: str
    fecha_solicitud: datetime

    class Config:
        from_attributes = True

class DevolucionUpdate(BaseModel):
    estado: str
