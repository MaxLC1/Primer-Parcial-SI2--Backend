from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from . import schemas, services

router = APIRouter(tags=["Reservas"])

@router.get("/", response_model=List[schemas.ReservaOut])
def read_reservas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtiene la lista de reservas registradas."""
    return services.get_reservas(db, skip=skip, limit=limit)

@router.post("/", response_model=schemas.ReservaOut, status_code=status.HTTP_201_CREATED)
def create_reserva(reserva: schemas.ReservaCreate, db: Session = Depends(get_db)):
    """Crea una nueva reserva con múltiples prendas."""
    return services.create_reserva(db=db, reserva=reserva)

@router.patch("/{reserva_id}/estado", response_model=schemas.ReservaOut)
def update_estado(reserva_id: int, estado: str, db: Session = Depends(get_db)):
    """Actualiza el estado de la reserva (Pendiente, Preparada, Cancelada, Completada)."""
    return services.update_estado_reserva(db=db, reserva_id=reserva_id, estado=estado)
