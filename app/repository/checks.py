from sqlalchemy.orm import Session
from sqlalchemy import asc 
from app.db import models
from fastapi import HTTPException,status 
from app.hashing import Hash
from core.utiles import ( validar_campos, validar_cadena,validar_sexo,validar_entero,validar_identificacion 
                         ,validar_telefono,validar_fecha,validar_email,validar_booleano, validar_password)


def check_username(username: str, db:Session):
    usuario_db = db.query(models.ApiUser).filter(models.ApiUser.username == username).first()
    if usuario_db:
        print('existe')
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Ya existe un usuario con el username {username}"
        )

def check_email(email: str, db:Session):
    print('email')
    usuario_db = db.query(models.Users).filter(models.Users.email == email).first()
    if usuario_db:
        print('existe')
        print(email)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Ya existe un usuario con el email {email}"
        )


def check_dni(dni: str, db:Session):
    usuario_db = db.query(models.Users).filter(models.Users.dni == dni).first()
    if usuario_db:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Ya existe un usuario con el dni {dni}"
        )



# Crear función que generará un token para la recuperación de contraseña
def new_token_password(email:str,db:Session):
    usuario = db.query(models.Usuario).filter(models.Usuario.email == email ).first()
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No existe el usuario con el email {email}"
        )
    token = Hash.generate_password_reset_token(email)
    campos_db = {
        "email": email,
        "token": token
    }
    print(token)
    try:
        nuevo_token = models.ResetPassword(**campos_db)
        db.add(nuevo_token)
        db.commit()
        db.refresh(nuevo_token)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Error creando token {e}"
        )
    return {"respuesta":"Token creado correctamente!"}
