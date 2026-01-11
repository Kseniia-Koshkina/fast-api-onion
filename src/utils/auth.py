import os
import bcrypt
from dotenv import load_dotenv

load_dotenv() 

secret_key = os.getenv("SECRET_KEY")
algorithm = os.getenv("ALGORITHM")

def generate_password_hash(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def verify_password(plain_password: str, hashed_password: str) -> bool:
	return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())