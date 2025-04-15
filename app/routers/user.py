from fastapi import APIRouter,Depends,status 
from app.schemas import sch_createApiUser, createUser, User
from app.db.database import get_db
from sqlalchemy.orm import Session 
from typing import List
from app.repository import user 
from app.oauth import get_current_user

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

# @router.get('/',response_model=List[ShowUser],status_code=status.HTTP_200_OK)
# #def obtener_usuarios(db:Session = Depends(get_db),current_user: User = Depends(get_current_user)):
# def obtener_usuarios(db:Session = Depends(get_db),current_user: User = Depends(get_current_user)):
#     data = user.obtener_usuarios(db)
#     return data

@router.post('/',status_code=status.HTTP_201_CREATED)
# def newapiuser(usuario:createApiUser,db:Session = Depends(get_db),current_user: User = Depends(get_current_user)):
def newapiuser(usuario:sch_createApiUser,db:Session = Depends(get_db)):
    print('routes newapiuser')    
    """
    ## Descripción:
        · Función que crea un nuevo usuario en la base de datos.
    ## Parámetros:
        · usuario: dict -> Diccionario con los datos del usuario.
        · db: Session -> Sesión de la base de datos.
    ## Retorna:
        · None
    """    
    user.createApiUser(usuario,db)
    return {"respuesta":"Usuario creado satisfactoriamente!!"}

@router.post('/createUser',status_code=status.HTTP_201_CREATED)
def createUser(usuario:createUser,db:Session = Depends(get_db)):
    print('routes createUser')
    user.createUser(usuario,db)
    return {"respuesta":"Usuario creado satisfactoriamente!!"}



# @router.get('/{user_id}',response_model=User,status_code=status.HTTP_200_OK)
# def obtener_usuario(user_id:int,db:Session = Depends(get_db),current_user: User = Depends(get_current_user)):
#     usuario = user.obtener_usuario(user_id,db)
#     return usuario

# @router.get('/byEmail/{email}',response_model=User,status_code=status.HTTP_200_OK)
# def obtener_usuario_x_email(email:str,db:Session = Depends(get_db)):
#     print(email)
#     email = user.obtener_usuario_x_email(email,db)
#     print(email)
#     return email

# @router.delete('/',status_code=status.HTTP_200_OK)
# def eliminar_usuario(user_id:int,db:Session = Depends(get_db)):
#     res = user.eliminar_usuario(user_id, db)
#     return res 

# @router.patch('/{user_id}',status_code=status.HTTP_200_OK)
# def actualizar_user(user_id:int,updateUser:UpdateUser,db:Session = Depends(get_db)):
#     res = user.actualizar_user(user_id,updateUser, db)
#     return res 

# @router.patch('/password/{user_id}',status_code=status.HTTP_200_OK)
# def actualizar_password(user_id:int,updateUserPassword:UpdateUserPassword,db:Session = Depends(get_db)):
#     res = user.actualizar_password(user_id,updateUserPassword, db)
#     return res 

# @router.post('/newtokenpassword/{email}',status_code=status.HTTP_200_OK)
# def new_token_password(email:str,db:Session = Depends(get_db)):
#     res = user.new_token_password(email, db)
#     return res