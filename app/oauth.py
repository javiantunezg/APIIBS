from fastapi import Depends,HTTPException,status 
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.token import verify_token
from app.schemas import TokenData
from app.db.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="v1/login")

def get_current_user(token: str = Depends(oauth2_scheme)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return verify_token(token)

# Crear una dependencia para verificar el rol
def rol_required(rol: str):
    def rol_checker(user: TokenData = Depends(get_current_user)):
        if user.rol != rol:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tienes permisos suficientes",
            )
        return user
    return rol_checker