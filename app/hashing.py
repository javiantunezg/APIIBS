import hashlib
from passlib.context import CryptContext
import time

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

class Hash():

    @staticmethod
    def md5_hash(contrasena):
        print(contrasena.encode())
        print(hashlib.md5(contrasena.encode()))
        print(hashlib.md5(contrasena.encode()).hexdigest())
        return hashlib.md5(contrasena.encode()).hexdigest()

    @staticmethod
    def hash_password(password):
        print(password)
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)
    
    @staticmethod
    def verify_password_md5(plain_password, hashed_password):
        plain_password_hashed = hashlib.md5(plain_password.encode()).hexdigest()
        print(plain_password_hashed)
        return plain_password_hashed == hashed_password
    
    @staticmethod
    def generate_password_reset_token(email):
        # Concatenar la variable email con los milisegundos actuales
        # Cifrar la cadena resultante con bcrypt
        cadena = email + str(time.time())
        cadenaCifrada = hashlib.md5(cadena.encode()).hexdigest()
        return cadenaCifrada
