from sqlalchemy.orm import Session
from sqlalchemy import asc 
from app.db import models
from fastapi import HTTPException,status 
from app.hashing import Hash
from app.schemas import sch_getBasicEvento



# Obtener todos los eventos devolviendo sólo los datos del esquema sch_getBasicEvento
def get_eventos_basic(db:Session):
    """
        · Descripción:
            # Función que obtiene todos los eventos de la base de datos.
        · Parámetros:
            # db: Session -> Sesión de la base de datos.
        · Retorna:
            # List[models.Evento] -> Lista de eventos.
    """
    eventos = db.query(models.Evento).order_by(asc(models.Evento.id_evento)).all()
    return [sch_getBasicEvento.from_orm(evento) for evento in eventos]