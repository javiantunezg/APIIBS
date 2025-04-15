import re
from fastapi import HTTPException,status 

def validar_identificacion(identificacion):
    # Expresiones regulares para validar cada tipo de identificación
    dni_espanol_pattern = r'^\d{8}[A-Za-z]$'
    nie_espanol_pattern = r'^[XYZ]\d{7}[A-Za-z]$'
    dni_portugues_pattern = r'^\d{9}$'
    dni_frances_pattern = r'^\d{2}[ \-]?\d{2}[ \-]?\d{2}[ \-]?\d{3}[ \-]?[0-9A-Za-z]{1,2}$'

    # Validación para DNI español
    if re.match(dni_espanol_pattern, identificacion):
        return True

    # Validación para NIE español
    if re.match(nie_espanol_pattern, identificacion):
        return True

    # Validación para DNI portugués
    if re.match(dni_portugues_pattern, identificacion):
        return True

    # Validación para DNI francés
    if re.match(dni_frances_pattern, identificacion):
        return True

    # Si no coincide con ninguno de los patrones anteriores, retorna False
    return False

def validar_telefono(numero):
    # Expresiones regulares para validar números de teléfono
    telefono_portugues_pattern = r'^(\+?351)?\d{9}$'  # Prefijo +351 opcional
    telefono_espanol_pattern = r'^(\+?34)?\d{9}$'     # Prefijo +34 opcional
    telefono_frances_pattern = r'^(\+?33)?\d{9}$'      # Prefijo +33 opcional

    # Validación para número de teléfono portugués
    if re.match(telefono_portugues_pattern, numero):
        return True, "Portugués"

    # Validación para número de teléfono español
    if re.match(telefono_espanol_pattern, numero):
        return True, "Español"

    # Validación para número de teléfono francés
    if re.match(telefono_frances_pattern, numero):
        return True, "Francés"

    # Si no coincide con ninguno de los patrones anteriores, retorna False
    return False, None

def validar_sexo(valor):
    if valor.lower() == "h" or valor.lower() == "m":
        return True
    return False

def validar_fecha(fecha):
    # Expresión regular para validar fechas en formato 'YYYY-MM-DD'
    # Convertimos la fecha a un string para poder compararla con el patrón
    fecha = fecha.strftime("%Y-%m-%d")
    fecha_pattern = r'^\d{4}-\d{2}-\d{2}$'

    # Validación para fechas en formato 'YYYY-MM-DD'
    if re.match(fecha_pattern, fecha):
        return True
    return False

def validar_cadena(cadena):
    # Expresión regular para validar cadenas de texto eliminando caracteres de escape
    cadena_pattern = r'^[a-zA-Z0-9\sáéíóúÁÉÍÓÚñÑüÜ.,;:¡!¿?@#%&()=+*ºª]{1,100}$'

    # Validación para cadenas de texto
    if re.match(cadena_pattern, cadena):
        return True
    return False

# Validamos un número
def validar_entero(numero):
    # Validación para números
    numero = str(numero)
    if isinstance(numero, str) and numero.isdigit():
        return True
    return False

def validar_email(email):
    # Expresión regular para validar correos electrónicos
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Validación para correos electrónicos
    if re.match(email_pattern, email):
        return True
    return False

def validar_password(password):
    # Expresión regular para validar contraseñas
    password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

    # Validación para contraseñas
    if re.match(password_pattern, password):
        return True
    return False

def validar_booleano(valor):
    if isinstance(valor, bool):
        return True
    return False

def validar_campos(campos_validacion, array_datos):
    for campo, validador in campos_validacion.items():
        if campo in array_datos and not validador(array_datos[campo]):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"{campo.capitalize()} no válido."
            )
    return True



