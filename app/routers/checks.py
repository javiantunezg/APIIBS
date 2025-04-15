from fastapi import APIRouter,Depends,status 
from app.db.database import get_db
from sqlalchemy.orm import Session 
from typing import List
from app.repository import checks 
from app.oauth import get_current_user



router = APIRouter(
    prefix="/checks",
    tags=["checks"]
)

@router.get("/username/{username}")
def check_username(username: str, db:Session = Depends(get_db)):
    checks.check_username(username, db)
    return {"respuesta":"Usuario disponible"}

@router.get("/email/{email}")
def check_email(email: str, db:Session = Depends(get_db)):
    checks.check_email(email, db)
    return {"respuesta":"Email disponible"}

@router.get("/dni/{dni}")
def check_dni(dni: str, db:Session = Depends(get_db)):
    checks.check_dni(dni, db)
    return {"respuesta":"DNI disponible"}   
