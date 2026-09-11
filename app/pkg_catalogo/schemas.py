from pydantic import BaseModel
from typing import Optional, List

# -- CATEGORIAS --
class ColeccionBase(BaseModel):
    nombre: str

class ColeccionCreate(ColeccionBase):
    pass

class ColeccionOut(ColeccionBase):
    id: int
    class Config:
        from_attributes = True

# -- PROVEEDORES --
class ProveedorBase(BaseModel):
    nombre: str
    contacto: Optional[str] = None

class ProveedorCreate(ProveedorBase):
    pass

class ProveedorOut(ProveedorBase):
    id: int
    class Config:
        from_attributes = True

# -- CATEGORIAS --
class CategoriaBase(BaseModel):
    nombre: str

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaOut(CategoriaBase):
    id: int
    class Config:
        from_attributes = True

# -- TALLAS --
class TallaBase(BaseModel):
    nombre: str

class TallaCreate(TallaBase):
    pass

class TallaOut(TallaBase):
    id: int
    class Config:
        from_attributes = True

# -- COLORES --
class ColorBase(BaseModel):
    nombre: str
    codigo_hex: Optional[str] = None

class ColorCreate(ColorBase):
    pass

class ColorOut(ColorBase):
    id: int
    class Config:
        from_attributes = True

# -- TEMPORADAS --
class TemporadaBase(BaseModel):
    nombre: str
    activa: bool = True

class TemporadaCreate(TemporadaBase):
    pass

class TemporadaOut(TemporadaBase):
    id: int
    class Config:
        from_attributes = True

# -- PRODUCTOS --
class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    categoria_id: Optional[int] = None
    modelo_3d_url: Optional[str] = None
    imagen_url: Optional[str] = None
    temporada_id: Optional[int] = None
    coleccion_id: Optional[int] = None
    proveedor_id: Optional[int] = None

class ProductoCreate(ProductoBase):
    pass

class ProductoOut(ProductoBase):
    id: int
    categoria: Optional[CategoriaOut] = None
    temporada: Optional[TemporadaOut] = None
    coleccion: Optional[ColeccionOut] = None
    proveedor: Optional[ProveedorOut] = None

    class Config:
        from_attributes = True
