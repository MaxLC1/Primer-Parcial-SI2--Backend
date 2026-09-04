from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Ciudad(Base):
    __tablename__ = "ciudades"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, nullable=False)
    
    sucursales = relationship("Sucursal", back_populates="ciudad")

class Sucursal(Base):
    __tablename__ = "sucursales"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    direccion = Column(String(200))
    ciudad_id = Column(Integer, ForeignKey("ciudades.id"))
    
    ciudad = relationship("Ciudad", back_populates="sucursales")
    inventarios = relationship("Inventario", back_populates="sucursal")

class Inventario(Base):
    __tablename__ = "inventarios"
    id = Column(Integer, primary_key=True, index=True)
    sucursal_id = Column(Integer, ForeignKey("sucursales.id"), nullable=False)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    talla_id = Column(Integer, ForeignKey("tallas.id"), nullable=False)
    color_id = Column(Integer, ForeignKey("colores.id"), nullable=False)
    cantidad = Column(Integer, default=0)

    sucursal = relationship("Sucursal", back_populates="inventarios")
    # Relaciones directas para facilitar consultas (CU-10 Disponibilidad)
    producto = relationship("Producto")
    talla = relationship("Talla")
    color = relationship("Color")
