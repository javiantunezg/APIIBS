from fastapi import APIRouter,Depends,status 
from app.schemas import sch_getBasicEvento
from datetime import datetime
from app.db.database import get_db
from sqlalchemy.orm import Session 
from typing import List
from app.repository import evento 
from app.oauth import get_current_user

router = APIRouter(
    prefix="/evento",
    tags=["Eventos"]
)

@router.get('/', response_model=List[sch_getBasicEvento], status_code=status.HTTP_200_OK)
# def eventos(db:Session = Depends(get_db),current_user: User = Depends(get_current_user)):
def eventos(db:Session = Depends(get_db)):
    """
        · Descripción:
            # Función que obtiene todos los eventos de la base de datos.
        · Parámetros:
            # db: Session -> Sesión de la base de datos.
        · Retorna:
            # List[models.Evento] -> Lista de eventos.
    """
    eventos = evento.get_eventos_basic(db)
    # si la fecha del evento es anterior a la actual el valor isPast será True
    for evento in eventos:
        if evento.fecha_evento < datetime.now():
            evento.isPast = True
        else:
            evento.isPast = False
    return eventos
