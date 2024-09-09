from fastapi import APIRouter
from schemas import UserBase, ArticleBase, ArticleDisplay, UserCurrent
from db.db_user import create_user
from fastapi import Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article
from typing import List
from auth.oauth2 import oauth2_scheme
from auth.oauth2 import get_current_user

router = APIRouter(prefix='/article', 
                   tags=['articles']
                   )

#article
@router.post('/', response_model=ArticleDisplay)
def create_article( request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)


@router.get('/{id}')
def get_article(id: int, db: Session= Depends(get_db), current_user: UserCurrent = Depends(get_current_user)):
    return {
        "data": db_article.get_article(db, id),
        "current_user": {
            current_user.email,
            current_user.username
        }
    }