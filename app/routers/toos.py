from fastapi import APIRouter,Depends,status 
from sqlalchemy.orm import Session 
from typing import List
from app.db.database import get_db
from app.schemas import Login
from app.repository import auth 
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/tools",
    tags=["tools"]
)

# @router.post('/',response_model=List[ShowUser],status_code=status.HTTP_200_OK)
# #def obtener_usuarios(db:Session = Depends(get_db),current_user: User = Depends(get_current_user)):
# def enviar_email(db:Session = Depends(get_db)):
#     data = user.obtener_usuarios(db)
#     return data