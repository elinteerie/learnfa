from fastapi import APIRouter
from schemas import UserBase, ArticleBase, ArticleDisplay
from db.db_user import create_user
from fastapi import Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article
from typing import List

router = APIRouter(prefix='/article', 
                   tags=['articles']
                   )

#article
@router.post('/', response_model=ArticleDisplay)
def create_article( request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)


@router.get('/{id}', response_model=ArticleDisplay)
def get_article(id: int, db: Session= Depends(get_db)):
    return db_article.get_article(db, id)