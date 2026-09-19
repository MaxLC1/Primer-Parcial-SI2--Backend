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

def update_producto(db: Session, producto_id: int, producto_data: schemas.ProductoCreate):
    db_producto = db.query(models.Producto).filter(models.Producto.id == producto_id).first()
    if db_producto:
        for key, value in producto_data.model_dump().items():
            setattr(db_producto, key, value)
        db.commit()
        db.refresh(db_producto)
    return db_producto

# -- CATEGORIAS --
def get_categorias(db: Session):
    return db.query(models.Categoria).all()

def create_categoria(db: Session, categoria: schemas.CategoriaCreate):
    db_categoria = models.Categoria(**categoria.model_dump())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def update_categoria(db: Session, categoria_id: int, categoria_data: schemas.CategoriaCreate):
    db_categoria = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()
    if db_categoria:
        for key, value in categoria_data.model_dump().items():
            setattr(db_categoria, key, value)
        db.commit()
        db.refresh(db_categoria)
    return db_categoria

def delete_categoria(db: Session, categoria_id: int):
    db_categoria = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()
    if db_categoria:
        try:
            db.delete(db_categoria)
            db.commit()
            return True
        except Exception:
            db.rollback()
            return False
    return False

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

# -- COLECCIONES --
def get_colecciones(db: Session):
    return db.query(models.Coleccion).all()

def create_coleccion(db: Session, coleccion: schemas.ColeccionCreate):
    db_coleccion = models.Coleccion(nombre=coleccion.nombre)
    db.add(db_coleccion)
    db.commit()
    db.refresh(db_coleccion)
    return db_coleccion

def update_coleccion(db: Session, coleccion_id: int, coleccion_data: schemas.ColeccionUpdate):
    db_coleccion = db.query(models.Coleccion).filter(models.Coleccion.id == coleccion_id).first()
    if db_coleccion:
        for key, value in coleccion_data.model_dump().items():
            setattr(db_coleccion, key, value)
        db.commit()
        db.refresh(db_coleccion)
    return db_coleccion

def delete_coleccion(db: Session, coleccion_id: int):
    db_coleccion = db.query(models.Coleccion).filter(models.Coleccion.id == coleccion_id).first()
    if db_coleccion:
        try:
            db.delete(db_coleccion)
            db.commit()
            return True
        except Exception:
            db.rollback()
            return False
    return False

# -- PROVEEDORES --
def get_proveedores(db: Session):
    return db.query(models.Proveedor).all()

def create_proveedor(db: Session, proveedor: schemas.ProveedorCreate):
    db_proveedor = models.Proveedor(nombre=proveedor.nombre, contacto=proveedor.contacto)
    db.add(db_proveedor)
    db.commit()
    db.refresh(db_proveedor)
    return db_proveedor

def update_proveedor(db: Session, proveedor_id: int, proveedor_data: schemas.ProveedorUpdate):
    db_proveedor = db.query(models.Proveedor).filter(models.Proveedor.id == proveedor_id).first()
    if db_proveedor:
        for key, value in proveedor_data.model_dump().items():
            setattr(db_proveedor, key, value)
        db.commit()
        db.refresh(db_proveedor)
    return db_proveedor
