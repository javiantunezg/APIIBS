import os 
from dotenv import load_dotenv
from pathlib import Path 
from urllib.parse import quote

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME:str = "REGISTRA-FACIL-API"
    PROJECT_VERSION:str = "1.0"
    USER: str = "ibsmoto"
    PASSWORD: str = "s1ST3M0S2023*"
    HOST: str = "localhost"
    DATABASE: str = "qafx088"
    DATABASE_URL: str = f"mysql+mysqlconnector://{USER}:{quote(PASSWORD)}@{HOST}/{DATABASE}"

    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_TLS: bool = True
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
        

settings = Settings()
