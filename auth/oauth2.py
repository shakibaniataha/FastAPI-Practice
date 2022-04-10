from datetime import timedelta, datetime
from typing import Optional
from fastapi.security import OAuth2PasswordBearer
from jose import jwt


oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/token")

SECRET_KEY = "4d8581d1a8f7ebe2de0c2de6811185f14f2c62add85b1e3e6ba2f4005f9b1dc4"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
