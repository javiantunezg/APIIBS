
from app.db.database import Base
from sqlalchemy import Column,Integer,String , Boolean, Date, TIMESTAMP, Text, JSON, Float
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

class UserTypes(Base):
    __tablename__ = "usertypes"
    
    idUserType = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

class ApiUser(Base):
    __tablename__ = "apiuser"
    
    idApiUser = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    passwordHash = Column(String, nullable=False)
    loginCount = Column(Integer, default=0)
    lastLogin = Column(TIMESTAMP, nullable=True)
    idUserType = Column(Integer, ForeignKey("usertypes.idUserType"), nullable=False)
    createdBy = Column(Integer, ForeignKey("apiuser.idApiUser"), nullable=True)
    # createdAt = Column(TIMESTAMP)
    updatedBy = Column(Integer, ForeignKey("apiuser.idApiUser"), nullable=True)
    # updatedAt = Column(TIMESTAMP)
    status = Column(Integer, default=1)
    
    userType = relationship("UserTypes")

class Users(Base):
    __tablename__ = "users"
    
    idUser = Column(Integer, primary_key=True, index=True)
    apiUserId = Column(Integer, ForeignKey("apiuser.idApiUser"), nullable=False)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    dni = Column(String, unique=True, nullable=False)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    postalCode = Column(String, nullable=False)
    state = Column(String, nullable=False)
    country = Column(String, nullable=False)
    birthDate = Column(Date, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)
    createdBy = Column(Integer, ForeignKey("apiuser.idApiUser"), nullable=True)
    # createdAt = Column(TIMESTAMP)
    updatedBy = Column(Integer, ForeignKey("apiuser.idApiUser"), nullable=True)
    # updatedAt = Column(TIMESTAMP)
    isActive = Column(Boolean, default=True)
    
    apiUser = relationship("ApiUser", foreign_keys=[apiUserId])
    creator = relationship("ApiUser", foreign_keys=[createdBy])
    updater = relationship("ApiUser", foreign_keys=[updatedBy])

class Evento(Base):
    __tablename__ = "eventos"

    id_evento = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    imagen = Column(String(200), nullable=False)
    poblacion = Column(String(50), nullable=False)
    fecha_evento = Column(Date, nullable=False)
    estado = Column(String(10), nullable=False)
    inscripciones = Column(String(15), nullable=False)
    fecha_veteranos = Column(Date, nullable=False)
    precio_general_taquilla = Column(Float, nullable=False)
    precio_acom = Column(Float, nullable=False)
    precio_road_book_rollo = Column(Integer, nullable=False)
    precio_road_book_a5 = Column(Integer, nullable=False)
    desc_corta = Column(Text, nullable=False)
    texto_previo = Column(Text, nullable=False)
    texto_grande = Column(Text, nullable=False)
    tipo_evento = Column(String(50), nullable=False, default='challenge')
    Visible = Column(Boolean, nullable=False, default=False)
    bases = Column(String(100), nullable=False)
    texto_fecha = Column(String(50), nullable=False)
    activo = Column(String(15), nullable=False, default='inactivo')
    modified_at = Column(TIMESTAMP, nullable=True)
    fecha_oros = Column(Date, nullable=True)
    fecha_apertura = Column(Date, nullable=True)
    fecha_general = Column(Date, nullable=True)
    plazas_libres = Column(Integer, nullable=True)
    precio_platino = Column(Float, nullable=True)
    precio_oro = Column(Float, nullable=True)
    precio_veterano = Column(Float, nullable=True)
    precio_general = Column(Float, nullable=True)
    precio_caja_12mm = Column(Float, nullable=True)
    precio_caja_ram = Column(Float, nullable=True)
    precio_mando_normal = Column(Float, nullable=True)
    precio_mando_pro = Column(Float, nullable=True)
    precio_cena_viernes = Column(Float, nullable=True)
    precio_cena_sabado = Column(Float, nullable=True)
    visible_cena_viernes = Column(Integer, default=0)
    visible_cena_sabado = Column(Integer, default=0)
    fecha_cierre = Column(Date, nullable=True)