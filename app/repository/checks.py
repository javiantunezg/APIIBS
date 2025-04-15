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



# def actualizar_password(user_id,updateUserPassword,db:Session):
#     #validamos que el user_id sea numérico utilizando las funciones de validación de core.utiles
#     if not validar_entero(user_id):
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail=f"El id de usuario debe ser un número."
#         )

#     instancia_usr = db.query(models.Usuario).filter(models.Usuario.id_usuario == user_id )
#     if not instancia_usr.first():
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"No existe el usuario con el id {user_id}"
#         )
#     instancia_usr.update({"password":Hash.hash_password(updateUserPassword.contrasena), "contrasena":Hash.md5_hash(updateUserPassword.contrasena)})
#     db.commit()
#     return {"respuesta":"Contraseña actualizada correctamente!"}

# def obtener_usuarios(db:Session):
#     data = db.query(models.Usuario).order_by(asc(models.Usuario.dorsal)).all()
#     return data

# def obtener_usuario(user_id,db:Session):
#     instancia_usr = db.query(models.Usuario).filter(models.Usuario.id_usuario == user_id ).first()
#     print(instancia_usr)
#     if not instancia_usr:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"No existe el usuario con el id {user_id}"
#         )
#     return instancia_usr

# def obtener_usuario_x_email(email:str,db:Session):
#     print("entro")
#     instancia_usr = db.query(models.Usuario).filter(models.Usuario.email == email ).first()
#     print("salgo")
#     if not instancia_usr:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"No existe el usuario con el email {email}"
#         )
#     return instancia_usr

# def eliminar_usuario(user_id,db:Session):
#     usuario = db.query(models.User).filter(models.User.id == user_id )
#     if not usuario.first():
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"No existe el usuario con el id {user_id} por lo tanto no se elimina"
#         )
#     usuario.delete(synchronize_session=False)
#     db.commit()
#     return {"respuesta":"Usuario eliminado correctamente!"}



# def actualizar_user(user_id,updateUser,db:Session):
#     usuario = db.query(models.User).filter(models.User.id == user_id )
#     if not usuario.first():
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"No existe el usuario con el id {user_id}"
#         )
#     usuario.update(updateUser.dict( exclude_unset=True))
#     db.commit()
#     return {"respuesta":"Usuario actualizado correctamente!"}


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
