from sqlalchemy.orm import Session
from . import models, schemas

# -- PRODUCTOS --
def get_productos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Producto).offset(skip).limit(limit).all()

def create_producto(db: Session, producto: schemas.ProductoCreate):
    db_producto = models.Producto(**producto.model_dump())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

# -- CATEGORIAS --
def get_categorias(db: Session):
    return db.query(models.Categoria).all()

def create_categoria(db: Session, categoria: schemas.CategoriaCreate):
    db_categoria = models.Categoria(nombre=categoria.nombre)
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

# -- TALLAS --
def get_tallas(db: Session):
    return db.query(models.Talla).all()

def create_talla(db: Session, talla: schemas.TallaCreate):
    db_talla = models.Talla(nombre=talla.nombre)
    db.add(db_talla)
    db.commit()
    db.refresh(db_talla)
    return db_talla

# -- COLORES --
def get_colores(db: Session):
    return db.query(models.Color).all()

def create_color(db: Session, color: schemas.ColorCreate):
    db_color = models.Color(nombre=color.nombre, codigo_hex=color.codigo_hex)
    db.add(db_color)
    db.commit()
    db.refresh(db_color)
    return db_color
