import bcrypt
import passlib
from passlib.context import CryptContext

print(bcrypt.__version__)
print(passlib.__version__)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
hashed = pwd_context.hash("mysecretpassword")
print(hashed)