
from app.db.database import Base
from sqlalchemy import Column,Integer,String , Boolean, Date, TIMESTAMP, Text, JSON
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
