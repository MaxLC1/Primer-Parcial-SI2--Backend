from sqlalchemy.orm import Session
from . import models, schemas

# -- CIUDADES --
def get_ciudades(db: Session):
    return db.query(models.Ciudad).all()

def create_ciudad(db: Session, ciudad: schemas.CiudadCreate):
    db_ciudad = models.Ciudad(nombre=ciudad.nombre)
    db.add(db_ciudad)
    db.commit()
    db.refresh(db_ciudad)
    return db_ciudad

# -- SUCURSALES --
def get_sucursales(db: Session):
    return db.query(models.Sucursal).all()

def create_sucursal(db: Session, sucursal: schemas.SucursalCreate):
    db_sucursal = models.Sucursal(**sucursal.model_dump())
    db.add(db_sucursal)
    db.commit()
    db.refresh(db_sucursal)
    return db_sucursal

# -- INVENTARIOS --
def get_inventarios(db: Session):
    return db.query(models.Inventario).all()

def create_inventario(db: Session, inventario: schemas.InventarioCreate):
    # Buscar si ya existe la combinacion
    db_inv = db.query(models.Inventario).filter(
        models.Inventario.sucursal_id == inventario.sucursal_id,
        models.Inventario.producto_id == inventario.producto_id,
        models.Inventario.talla_id == inventario.talla_id,
        models.Inventario.color_id == inventario.color_id
    ).first()

    if db_inv:
        db_inv.cantidad += inventario.cantidad
        db.commit()
        db.refresh(db_inv)
        return db_inv

    db_nuevo = models.Inventario(**inventario.model_dump())
    db.add(db_nuevo)
    db.commit()
    db.refresh(db_nuevo)
    return db_nuevo
