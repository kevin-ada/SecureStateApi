from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends
from jose import jwt, JWTError
from database import models, schema
from datetime import datetime, timedelta
from config import settings
from database.db_conn import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"expire": expire.strftime("%Y-%m-%d %H-%M-%S")})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)

        token_id: str = str(payload.get("user_id"))

        if id is None:
            raise credentials_exception

        token_data = schema.DataToken(token_id=token_id)
    except JWTError as e:
        print(e)
        raise credentials_exception

    return token_data


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not validate credentials",
                                          headers={"WWW-Authenticate": "Bearer"}
                                          )

    token = verify_token(token, credentials_exception)

    user = db.query(models.Users).filter(models.Users.id == token.token_id).first()

    return user
