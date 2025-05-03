from fastapi import FastAPI, APIRouter
import uvicorn 
from app.db.database import Base,engine
from app.routers import auth, checks, evento, usuarios
from fastapi.middleware.cors import CORSMiddleware
from middlewares import token_middleware

app = FastAPI()

# app.add_middleware(token_middleware.TokenMiddleware)


# Crear un enrutador principal con el prefijo `/v1`
api_v1_router = APIRouter(prefix="/v1")

api_v1_router.include_router(auth.router)
api_v1_router.include_router(checks.router)
api_v1_router.include_router(evento.router)
api_v1_router.include_router(usuarios.router)

app.include_router(api_v1_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__=="__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)
