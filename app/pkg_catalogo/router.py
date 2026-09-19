from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from . import schemas, services

router = APIRouter(tags=["Catálogo"])

@router.get("/categorias", response_model=List[schemas.CategoriaOut])
def read_categorias(db: Session = Depends(get_db)):
    """Obtiene la lista de todas las categorías de ropa."""
    return services.get_categorias(db)

@router.post("/categorias", response_model=schemas.CategoriaOut, status_code=status.HTTP_201_CREATED)
def create_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    """Crea una nueva categoría."""
    return services.create_categoria(db=db, categoria=categoria)

@router.put("/categorias/{categoria_id}", response_model=schemas.CategoriaOut)
def update_categoria(categoria_id: int, categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    """Actualiza una categoría existente."""
    db_cat = services.update_categoria(db=db, categoria_id=categoria_id, categoria_data=categoria)
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return db_cat

@router.delete("/categorias/{categoria_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_categoria(categoria_id: int, db: Session = Depends(get_db)):
    """Elimina una categoría."""
    success = services.delete_categoria(db=db, categoria_id=categoria_id)
    if not success:
        raise HTTPException(status_code=404, detail="Categoría no encontrada o no se puede eliminar por integridad de datos")
    return None

@router.get("/productos", response_model=List[schemas.ProductoOut])
def read_productos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtiene el catálogo de productos con paginación."""
    return services.get_productos(db, skip=skip, limit=limit)

@router.post("/productos", response_model=schemas.ProductoOut, status_code=status.HTTP_201_CREATED)
def create_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    """Crea un nuevo producto en el catálogo."""
    return services.create_producto(db=db, producto=producto)

@router.put("/productos/{producto_id}", response_model=schemas.ProductoOut)
def update_producto(producto_id: int, producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    """Actualiza un producto existente en el catálogo."""
    db_producto = services.update_producto(db=db, producto_id=producto_id, producto_data=producto)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

@router.get("/tallas", response_model=List[schemas.TallaOut])
def read_tallas(db: Session = Depends(get_db)):
    """Obtiene la lista de tallas de ropa."""
    return services.get_tallas(db)

@router.post("/tallas", response_model=schemas.TallaOut, status_code=status.HTTP_201_CREATED)
def create_talla(talla: schemas.TallaCreate, db: Session = Depends(get_db)):
    """Registra una nueva talla."""
    return services.create_talla(db=db, talla=talla)

@router.get("/colores", response_model=List[schemas.ColorOut])
def read_colores(db: Session = Depends(get_db)):
    """Obtiene la lista de colores registrados."""
    return services.get_colores(db)

@router.post("/colores", response_model=schemas.ColorOut, status_code=status.HTTP_201_CREATED)
def create_color(color: schemas.ColorCreate, db: Session = Depends(get_db)):
    """Registra un nuevo color (nombre y HEX)."""
    return services.create_color(db=db, color=color)

# -- COLECCIONES --
@router.get("/colecciones", response_model=List[schemas.ColeccionOut])
def read_colecciones(db: Session = Depends(get_db)):
    """Obtiene la lista de colecciones."""
    return services.get_colecciones(db)

@router.post("/colecciones", response_model=schemas.ColeccionOut, status_code=status.HTTP_201_CREATED)
def create_coleccion(coleccion: schemas.ColeccionCreate, db: Session = Depends(get_db)):
    """Registra una nueva coleccion."""
    return services.create_coleccion(db=db, coleccion=coleccion)

@router.put("/colecciones/{coleccion_id}", response_model=schemas.ColeccionOut)
def update_coleccion(coleccion_id: int, coleccion: schemas.ColeccionUpdate, db: Session = Depends(get_db)):
    """Actualiza una colección existente."""
    db_col = services.update_coleccion(db=db, coleccion_id=coleccion_id, coleccion_data=coleccion)
    if db_col is None:
        raise HTTPException(status_code=404, detail="Colección no encontrada")
    return db_col

@router.delete("/colecciones/{coleccion_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_coleccion(coleccion_id: int, db: Session = Depends(get_db)):
    """Elimina una colección."""
    success = services.delete_coleccion(db=db, coleccion_id=coleccion_id)
    if not success:
        raise HTTPException(status_code=404, detail="Colección no encontrada o no se puede eliminar por integridad de datos")
    return None

# -- PROVEEDORES --
@router.get("/proveedores", response_model=List[schemas.ProveedorOut])
def read_proveedores(db: Session = Depends(get_db)):
    """Obtiene la lista de proveedores."""
    return services.get_proveedores(db)

@router.post("/proveedores", response_model=schemas.ProveedorOut, status_code=status.HTTP_201_CREATED)
def create_proveedor(proveedor: schemas.ProveedorCreate, db: Session = Depends(get_db)):
    """Registra un nuevo proveedor."""
    return services.create_proveedor(db=db, proveedor=proveedor)

@router.put("/proveedores/{proveedor_id}", response_model=schemas.ProveedorOut)
def update_proveedor(proveedor_id: int, proveedor: schemas.ProveedorUpdate, db: Session = Depends(get_db)):
    """Actualiza un proveedor existente."""
    db_prov = services.update_proveedor(db=db, proveedor_id=proveedor_id, proveedor_data=proveedor)
    if db_prov is None:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    return db_prov
