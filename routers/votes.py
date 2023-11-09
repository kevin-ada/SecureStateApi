from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from auth.oauth2 import get_current_user
from database import models
from database.schema import Vote
from database.db_conn import get_db

router = APIRouter(
    tags=['VOTING'],
    prefix='/votes'
)


@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_vote(vote:Vote,db: Session = Depends(get_db),current_user: int = Depends(get_current_user)):

    post = db.query(models.Posts).filter(models.Posts.id == vote.post_id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Well that's not expected, this post does "
                                                                          "not exist")
    vote_query = db.query(models.Votes).filter(models.Votes.post_id == vote.post_id,
                                               models.Votes.user_id == current_user.id)
    found_vote = vote_query.first()

    if vote.dir == 1:

        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"The User {current_user.id} has already voted for {vote.post_id}")
        new_vote = models.Votes(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"Message": "Nice, Like implemented successfully"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vote does not exist")
        vote_query.delete(synchronize_session=False)
        db.commit()

        return {"Message": "Damn That has been unliked"}
