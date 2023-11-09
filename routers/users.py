from typing import List
from utils import hash_password
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from database import schema, models
from database.db_conn import get_db

router = APIRouter(
    tags=['User Registration'],
    prefix="/users"
)


@router.post('/create', status_code=status.HTTP_201_CREATED, response_model=List[schema.UserOut])
def create_user(new_user: schema.RegUser, db: Session = Depends(get_db)):
    password = hash_password(new_user.password)
    new_user.password = password
    user = models.Users(**new_user.model_dump())
    db.add(user)
    db.commit()

    return [user]

@router.get('/all', status_code=status.HTTP_200_OK, response_model=List[schema.UserOut])
def get_all_users(db:Session = Depends(get_db)):
    user = db.query(models.Users).all()

    return user

