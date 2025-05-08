
from pydantic import BaseModel

from typing import Optional,Union, List, Dict, Any
from pydantic.networks import EmailStr # type: ignore
from datetime import datetime, date





#  -------------------------------- Usuarios Begin --------------------------------

class UsuarioBase(BaseModel):
    id_usuario: int
    nombre: Optional[str]
    apellidos: Optional[str]
    apellido2: Optional[str]
    email: Optional[str]
    telefono: Optional[str]
    dni: Optional[str]
    dorsal: Optional[int]
    rol: Optional[str]

class TokenData(BaseModel):
    sub: str
    rol: str
    id_usuario: int

class UsuarioCrear(UsuarioBase):
    pass

class UsuarioActualizar(BaseModel):
    nombre: Optional[str]
    apellidos: Optional[str]
    apellido2: Optional[str]
    email: Optional[EmailStr]
    telefono: Optional[str]
    dni: Optional[str]

class Usuario(BaseModel):
    id_usuario: int

    class Config:
        from_attributes = True


class UserOut(BaseModel):
    id_usuario: int
    email: str
    nombre: str
    apellidos: str
    sexo: str
    dni: Optional[str] = None  # Puede ser None
    fecha_nacimiento: Optional[date] = None
    estado: str
    dorsal: Optional[int] = None  # Puede ser None
    hobbies: str
    profesion: str
    telefono: str
    direccion: str
    poblacion: str
    cod_postal: str
    provincia: str
    pais: str
    version: int
    apellido2: str
    piloto: bool
    talla_camiseta: str
    marca_telefono: Optional[str] = None  # Puede ser None
    modelo_telefono: Optional[str] = None  # Puede ser None
    # created_at: datetime
    modified_at: datetime
    rol: str
    class Config:
        from_attributes = True

#  -------------------------------- Usuarios End --------------------------------

#  -------------------------------- Login & Tokens Begin --------------------------------
class Login(BaseModel):
    id_usuario:str 
    contrasena:str

class Token(BaseModel):
    access_token: str
    token_type: str

#  -------------------------------- Login & Tokens END --------------------------------





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