from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database import Base

class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, nullable=False)
    
    productos = relationship("Producto", back_populates="categoria")

class Temporada(Base):
    __tablename__ = "temporadas"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, nullable=False) # Ej: Verano 2026
    activa = Column(Boolean, default=True)
    
    productos = relationship("Producto", back_populates="temporada")

class Talla(Base):
    __tablename__ = "tallas"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(10), unique=True, nullable=False) # S, M, L, XL

class Color(Base):
    __tablename__ = "colores"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, nullable=False)
    codigo_hex = Column(String(7)) # #FFFFFF

class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(200), nullable=False)
    descripcion = Column(Text)
    precio = Column(Float, nullable=False)
    
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    temporada_id = Column(Integer, ForeignKey("temporadas.id"))
    
    # URL al archivo .glb o .usdz para Realidad Aumentada
    modelo_3d_url = Column(String(255), nullable=True)

    # Relación de vuelta a la categoría
    categoria = relationship("Categoria", back_populates="productos")
    temporada = relationship("Temporada", back_populates="productos")
