
from pydantic import BaseModel

from typing import Optional,Union
from datetime import datetime, date





#  -------------------------------- Login & Tokens Begin --------------------------------
class Login(BaseModel):
    id_usuario:str 
    contrasena:str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None

#  -------------------------------- Login & Tokens END --------------------------------



# class UpdateUser(BaseModel): #Schema 
#     username:str = None 
#     password:str = None 
#     nombre:str = None 
#     apellido:str = None 
#     telefono:int = None 
#     email:str = None 

# class UpdateUserPassword(BaseModel): #Schema 
#     id_usuario:int
#     contrasena:str = None 

# class ShowUser(BaseModel):
#     id_usuario:int
#     nombre:str 
#     apellidos:str
#     apellido2:str 
#     email:str
#     dorsal:Optional[int]
#     class Config():
#         from_attributes = True 




# -------------------------------- Evento --------------------------------
# -------------------------------- BEGIN --------------------------------

class sch_getBasicEvento(BaseModel):
    id_evento: int
    nombre: str
    imagen: str
    poblacion: str
    fecha_evento: datetime
    isPast: bool = False
    class Config:
        from_attributes = True

# -------------------------------- ENDS --------------------------------
# -------------------------------- Evento --------------------------------