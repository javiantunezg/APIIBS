
from app.db.database import Base
from sqlalchemy import Column,Integer,String , Boolean, Date, TIMESTAMP, Text, JSON, Float
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base


# MODELOS PARA USUARIOS


class User(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(60), unique=True, nullable=False)
    nombre = Column(String(30), nullable=False)
    apellidos = Column(String(50), nullable=False)
    sexo = Column(String(8), nullable=False)
    dni = Column(String(10), unique=True)
    contrasena = Column(String(100), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    estado = Column(String(15), nullable=False)
    dorsal = Column(Integer, unique=True)
    hobbies = Column(Text, nullable=False)
    profesion = Column(Text, nullable=False)
    telefono = Column(String(20), nullable=False)
    direccion = Column(String(100), nullable=False)
    poblacion = Column(String(50), nullable=False)
    cod_postal = Column(String(15), nullable=False)
    provincia = Column(String(50), nullable=False)
    pais = Column(String(30), nullable=False)
    version = Column(Integer, nullable=False)
    apellido2 = Column(String(50), nullable=False)
    piloto = Column(Boolean, nullable=False, default=True)
    talla_camiseta = Column(String(3), nullable=False)
    marca_telefono = Column(String(50))
    modelo_telefono = Column(String(50))
    # created_at = Column(TIMESTAMP, server_default=func.now())
    modified_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    rol = Column(String(50), default='usuario')

# MODELOS PARA EVENTOS
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