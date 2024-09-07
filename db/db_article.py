from sqlalchemy.orm.session import Session
from schemas import User, Article, ArticleDisplay, ArticleBase
from db.models import DbUser, DbArticle


def create_article(db: Session, request: ArticleBase):
    new_article = DbArticle(
        title= request.title,
        content = request.content,
        published = request.published,
        user_id = request.creator_id
        
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article 


def get_article(db:Session, id:int):
    article = db.query(DbArticle).filter(DbArticle.id == id).first()
    #handle errors
    return article