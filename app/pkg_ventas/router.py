from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from . import schemas, services

router = APIRouter(tags=["Ventas"])

@router.post("/", response_model=schemas.VentaOut)
def crear_venta(venta: schemas.VentaCreate, db: Session = Depends(get_db)):
    return services.create_venta(db=db, venta=venta)

@router.get("/", response_model=List[schemas.VentaOut])
def obtener_ventas(db: Session = Depends(get_db)):
    return services.get_ventas(db=db)
