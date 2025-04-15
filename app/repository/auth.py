from sqlalchemy.orm import Session 
from app.db import models
from fastapi import HTTPException,status 
from app.hashing import Hash
from app.token import create_access_token


def auth_user(usuario,db:Session):

    print (usuario.username,usuario.password)
    user = db.query(models.ApiUser).filter(models.ApiUser.username==usuario.username).first()
    print('1')

    if not user:
        print(4)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"""No existe el usuario con el username {usuario.username} por lo tanto no se realiza el login"""
        )
    print('2')
    print(user.passwordHash)
    if not user.passwordHash:
        if not Hash.verify_password(usuario.password, user.password):
            print('5')
            raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"""Contraseña incorrecta ! """
                )
        
    print('3')
    access_token = create_access_token(
        data={"sub": usuario.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}

