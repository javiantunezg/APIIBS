from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List, Dict
import aiosmtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from core.config import settings

app = FastAPI()

class EmailData(BaseModel):
    email: EmailStr
    additional_data: Dict[str, str]

class EmailRequest(BaseModel):
    asunto: str
    cuerpo: str
    destinatarios: List[EmailData]

async def enviar_correo(asunto: str, cuerpo: str, destinatario: EmailData):
    # Configura el servidor SMTP
    smtp_host = settings.smtp_host
    smtp_port = settings.smtp_port
    smtp_user = settings.smtp_user
    smtp_password = settings.smtp_password

    # Crear el mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = smtp_user
    mensaje['To'] = destinatario.email
    mensaje['Subject'] = asunto

    # Personalizar el cuerpo del correo
    cuerpo_personalizado = cuerpo.format(**destinatario.additional_data)

    mensaje.attach(MIMEText(cuerpo_personalizado, 'plain'))

    # Enviar el correo
    try:
        async with aiosmtplib.SMTP(hostname=smtp_host, port=smtp_port) as smtp:
            await smtp.login(smtp_user, smtp_password)
            await smtp.send_message(mensaje)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/enviar-correos/")
async def enviar_correos(request: EmailRequest):
    for destinatario in request.destinatarios:
        await enviar_correo(request.asunto, request.cuerpo, destinatario)
    return {"message": "Correos enviados exitosamente"}

# Para correr la aplicación
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)