import os
from time import time
import bcrypt
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from jose import jwt

load_dotenv() 

secret_key = os.getenv("SECRET_KEY")
algorithm = os.getenv("ALGORITHM")
token_expire_minutes = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

def generate_password_hash(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def verify_password(plain_password: str, hashed_password: str) -> bool:
	return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=token_expire_minutes)
    to_encode.update({
        "iss": "fastapi-onion-app",
        "exp": expire,
        "iat": datetime.now(timezone.utc),
        "username": data.get("username"),
    })

    encoded_jwt = jwt.encode(
        to_encode,
        secret_key,
        algorithm
    )

    return encoded_jwt