from sqlalchemy.orm import Session
from sqlalchemy import asc 
from app.db import models
from fastapi import HTTPException,status 
from app.hashing import Hash
from core.utiles import ( validar_campos, validar_cadena,validar_sexo,validar_entero,validar_identificacion 
                         ,validar_telefono,validar_fecha,validar_email,validar_booleano, validar_password)
from app.routers.checks import check_username,check_email,check_dni
from app.schemas import sch_createApiUser


def createApiUser(apiuser,db:Session):
    """
        · Descripción:
            # Función que crea un nuevo usuario en la base de datos.
        · Parámetros:
            # usuario: dict -> Diccionario con los datos del usuario.
            # db: Session -> Sesión de la base de datos.
        · Retorna:
            # None
    """
    usuario = apiuser.dict()
    campos_validacion = {
        "username": validar_cadena,
        "passwordHash": validar_password
    }

    validar_campos(campos_validacion, usuario)

    try:
        campos_db = {
            "username": usuario["username"],
            "passwordHash": Hash.hash_password(usuario["passwordHash"]),
            "loginCount": 0,
            "status": 1,
            "idUserType": usuario.get("idUserType"),
            "createdBy": usuario.get("createdBy")
        }
        
        nuevo_usuario = models.ApiUser(**campos_db)
        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)
        return nuevo_usuario.idApiUser
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Error creando usuario {e}"
        )


def createUser(user,db:Session):
    """
        · Descripción:
            # Función que crea un nuevo usuario en la base de datos.
        · Parámetros:
            # usuario: dict -> Diccionario con los datos del usuario.
            # db: Session -> Sesión de la base de datos.
        · Retorna:
            # None
    """

    # Con esta función vamos a crear 2 usuarios, uno de ellos en la tabla userapi con el que haremos login 
    # y otro en la tabla user con el que haremos el CRUD.
    # print(user)
    usuario = user.dict()
    campos_validacion = {
        "username": validar_cadena,
        "passwordHash": validar_cadena,
        "sexo": validar_sexo,
        "idUserType": validar_entero,
        "createdBy": validar_entero,
        "firstName": validar_cadena,
        "lastName": validar_cadena,
        "dni" : validar_identificacion,
        "address": validar_cadena,
        "city": validar_cadena,
        "postalCode": validar_cadena,
        "state": validar_cadena,
        "country": validar_cadena,
        "birthDate": validar_fecha,
        "email": validar_email,
        "phone": validar_telefono,
        "isActive": validar_booleano
    }

  
    # Una vez comprobado que todos los datos son correctos procedemos a almacenar la información
    # en cada tabla.
    # Esta operación debemos hacerla mediante una transación de forma que si el insert en la tabla users falla
    # el usuario apiuser no debe crearse
    # Comenzamos una transacción para mysql

    validar_campos(campos_validacion, usuario)
    check_username(usuario["username"], db)
    check_email(usuario["email"], db)
    check_dni(usuario["dni"], db)
 
    try:
 
        datos_usuario = sch_createApiUser(
            username = usuario["username"],
            passwordHash = usuario["passwordHash"],
            idUserType = usuario.get("idUserType"),
            createdBy = usuario.get("createdBy")
        )

        # Usamos la funcion createApiUser para crear el usuario en la tabla apiuser    
        idApiUser = createApiUser(datos_usuario,db)
        
        campos_db = {
            "apiUserId": idApiUser,
            "firstName": usuario["firstName"],
            "lastName": usuario["lastName"],
            "dni": usuario["dni"],
            "address": usuario["address"],
            "city": usuario["city"],
            "postalCode": usuario["postalCode"],
            "state": usuario["state"],
            "country": usuario["country"],
            "birthDate": usuario["birthDate"],
            "email": usuario["email"],
            "phone": usuario["phone"],
            "createdBy": usuario.get("createdBy"),
            "isActive": usuario.get("isActive")
        }
        
        nuevo_usuario = models.Users(**campos_db)
        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Error creando usuario - : {str(e)}"
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
