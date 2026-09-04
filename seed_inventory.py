import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.core.database import SessionLocal
from app.pkg_sucursales.models import Inventario
from app.pkg_catalogo.models import Producto

def seed_inventory():
    db = SessionLocal()
    try:
        productos = db.query(Producto).all()
        for p in productos:
            # Check if inventory exists for sucursal=1, talla=1, color=1
            inv = db.query(Inventario).filter_by(
                sucursal_id=1,
                producto_id=p.id,
                talla_id=1,
                color_id=1
            ).first()
            
            if not inv:
                nuevo_inv = Inventario(
                    sucursal_id=1,
                    producto_id=p.id,
                    talla_id=1,
                    color_id=1,
                    cantidad=100
                )
                db.add(nuevo_inv)
                print(f"Inventario añadido para producto {p.nombre}")
            else:
                inv.cantidad = 100
                print(f"Inventario actualizado para producto {p.nombre}")
        
        db.commit()
        print("Inventario inicializado correctamente.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_inventory()
