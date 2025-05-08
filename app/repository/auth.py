from sqlalchemy.orm import Session 
from app.db import models
from fastapi import HTTPException,status 
from app.hashing import Hash
from app.token import create_access_token
from datetime import datetime


def auth_user(usuario,db:Session):

    print (usuario.username,usuario.password)
    user = db.query(models.User).filter(models.User.email==usuario.username).first()
    print('1')

    if not user:
        print(4)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"""No existe el usuario con el username {usuario.username} por lo tanto no se realiza el login"""
        )
    print('2')
    print(user.contrasena)
    if not Hash.verify_password_md5(usuario.password, user.contrasena):
        print('5')
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"""Contraseña incorrecta ! """
            )
        
    print('3')
    payload = {
        "sub": usuario.username,
        "rol": user.rol,
        "id_usuario": user.id_usuario  # ✅ Añadimos el ID del usuario
    }
    access_token = create_access_token(data=payload)
    return {"access_token": access_token, "token_type": "bearer"}

