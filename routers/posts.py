from fastapi import APIRouter, Depends, status, Response, HTTPException
from auth.oauth2 import get_current_user
from database import schema, models
from database.db_conn import get_db
from sqlalchemy.orm import Session
from typing import List, Optional

router = APIRouter(
    tags=['Posts'],
    prefix='/posts'
)


@router.post('/create', status_code=status.HTTP_201_CREATED, response_model=List[schema.RegOut])
def create_post(new_post: schema.RegPost, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    post = models.Posts(**new_post.model_dump(), user_id=current_user.id)

    db.add(post)
    db.commit()
    db.refresh(post)

    return [post]


@router.get('/all', status_code=status.HTTP_200_OK, response_model=List[schema.RegOut])
def get_all_posts(db: Session = Depends(get_db), search: Optional[str] = "", current_user: int = Depends(get_db)):
    posts = db.query(models.Posts).filter(models.Posts.title.ilike(f'%{search}%')).all()

    return posts


@router.get('/{id}')
def get_one_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(get_db)):
    post = db.query(models.Posts).filter(models.Posts.id == id).first()

    if not post:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The ID {id} with that number could not be found")

    return post


@router.post('/{posts_id}/images', status_code=status.HTTP_201_CREATED, response_model=List[schema.ImageOut])
def create_post_image(posts_id: int, image: schema.Image, current_user: int = Depends(get_current_user),
                      db: Session = Depends(get_db)):
    db_product = db.query(models.Posts).filter(models.Posts.id == posts_id)
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no Product with that id:{posts_id}")
    add_image = models.Images(**image.model_dump(), posts_id=posts_id)
    db.add(add_image)
    db.commit()

    return [add_image]


@router.get("/{posts_id}/images/", response_model=list[schema.RegPost])
def get_images_for_product(posts_id: int, db: Session = Depends(get_db)):
    db_product = db.query(models.Posts).filter(models.Posts.id == posts_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product.images