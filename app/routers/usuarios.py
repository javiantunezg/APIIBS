from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.db.models import User
from app.schemas import Usuario, UsuarioCrear, UsuarioActualizar, UsuarioBase, UserOut
from app.db.database import get_db
from app.oauth import get_current_user
from app.oauth import rol_required

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

# 1. Obtener todos los usuarios
@router.get("/", response_model=List[UsuarioBase])
def obtener_usuarios(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(User).all()

# 5. Obtener usuario por ID
@router.get("/{id_usuario}", response_model=UserOut)
def obtener_usuario_por_id(id_usuario: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    usuario = db.query(User).filter(User.id_usuario == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

# 2. Buscar usuario
@router.get("/buscar", response_model=List[Usuario])
def buscar_usuario(
    email: str = Query(None),
    dni: str = Query(None),
    telefono: str = Query(None),
    nombre: str = Query(None),
    apellidos: str = Query(None),
    apellido2: str = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user), 
    user: User = Depends(rol_required("administrador")),    
):
    query = db.query(User)
    if email:
        query = query.filter(User.email == email)
    if dni:
        query = query.filter(User.dni == dni)
    if telefono:
        query = query.filter(User.telefono == telefono)
    if nombre and apellidos and apellido2:
        query = query.filter(
            User.nombre == nombre,
            User.apellidos == apellidos,
            User.apellido2 == apellido2
        )
    usuarios = query.all()
    if not usuarios:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuarios

# 3. Crear usuario
@router.post("/", response_model=Usuario)
def crear_usuario(usuario: UsuarioCrear, db: Session = Depends(get_db)):
    nuevo_usuario = User(**usuario.dict())
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

# 4. Actualizar usuario
@router.put("/{id_usuario}", response_model=Usuario)
def actualizar_usuario(id_usuario: int, datos: UsuarioActualizar, db: Session = Depends(get_db)):
    usuario = db.query(User).filter(User.id_usuario == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    for key, value in datos.dict(exclude_unset=True).items():
        setattr(usuario, key, value)
    db.commit()
    db.refresh(usuario)
    return usuario



