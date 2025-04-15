from fastapi import APIRouter,Depends,status 
from app.schemas import sch_getBasicEvento
from app.db.database import get_db
from sqlalchemy.orm import Session 
from typing import List
from app.repository import evento 
from app.oauth import get_current_user

router = APIRouter(
    prefix="/evento",
    tags=["Eventos"]
)

# @router.get('/',response_model=List[ShowUser],status_code=status.HTTP_200_OK)
# #def obtener_usuarios(db:Session = Depends(get_db),current_user: User = Depends(get_current_user)):
# def obtener_usuarios(db:Session = Depends(get_db),current_user: User = Depends(get_current_user)):
#     data = user.obtener_usuarios(db)
#     return data

@router.get('/',status_code=status.HTTP_201_CREATED)
# def newapiuser(usuario:createApiUser,db:Session = Depends(get_db),current_user: User = Depends(get_current_user)):
def eventos(evento:sch_getBasicEvento,db:Session = Depends(get_db)):
    print('routes evento')    
    """
    ## Descripción:
        · Este endpoint permite obtener todos los eventos.
    ## Retorna:
        · None
    """    
    
    evento.get_eventos(db)
    return {"respuesta":"Usuario creado satisfactoriamente!!"}