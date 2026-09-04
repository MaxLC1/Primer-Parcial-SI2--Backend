from pydantic import BaseModel
from typing import Optional
from app.pkg_catalogo.schemas import ProductoOut, TallaOut, ColorOut

# -- CIUDADES --
class CiudadBase(BaseModel):
    nombre: str

class CiudadCreate(CiudadBase):
    pass

class CiudadOut(CiudadBase):
    id: int
    class Config:
        from_attributes = True

# -- SUCURSALES --
class SucursalBase(BaseModel):
    nombre: str
    direccion: Optional[str] = None
    ciudad_id: int

class SucursalCreate(SucursalBase):
    pass

class SucursalOut(SucursalBase):
    id: int
    ciudad: Optional[CiudadOut] = None

    class Config:
        from_attributes = True

# -- INVENTARIOS --
class InventarioBase(BaseModel):
    sucursal_id: int
    producto_id: int
    talla_id: int
    color_id: int
    cantidad: int

class InventarioCreate(InventarioBase):
    pass

class InventarioOut(InventarioBase):
    id: int
    sucursal: Optional[SucursalOut] = None
    producto: Optional[ProductoOut] = None
    talla: Optional[TallaOut] = None
    color: Optional[ColorOut] = None
    
    class Config:
        from_attributes = True
