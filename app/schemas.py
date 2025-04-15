
from pydantic import BaseModel

from typing import Optional,Union
from datetime import datetime, date



#  -------------------------------- User Begin --------------------------------
class sch_createApiUser(BaseModel):
    username: str
    passwordHash: str
    idUserType: int
    createdBy: int

class createUser(BaseModel):
    username: str
    passwordHash: str
    sexo: str
    idUserType: int
    createdBy: int
    firstName: str
    lastName: str
    dni: str
    address: str
    city: str
    postalCode: str
    state: str
    country: str
    birthDate: date
    email: str
    phone: str
    isActive: bool

class User(BaseModel):
    username: str
    passwordHash: Optional[str] = None
#  -------------------------------- User END --------------------------------




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
    fecha: datetime
    class Config:
        from_attributes = True

# -------------------------------- ENDS --------------------------------
# -------------------------------- Evento --------------------------------