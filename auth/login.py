from typing import List
from auth import oauth2
import utils
from database import db_conn, models, schema
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from database.db_conn import get_db

router = APIRouter(
    tags=['AUTHENTICATION'],
    prefix='/login'
)


@router.post('', status_code=status.HTTP_202_ACCEPTED, response_model=List[schema.Token])
def login(user_cred: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.email == user_cred.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="This user Does not exist")

    if not utils.verify_hashed_password(user_cred.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid User Credentials")

    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return [{
        "access_token": access_token,
        "token_type": "Bearer"
    }]
