from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from .hash import Hash
from fastapi import HTTPException, status



def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_all_users_a(db: Session):
    return db.query(DbUser).all()


def get_user_by_id(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id ==id).first()
    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not Found")
    return user


def update_user(db: Session, id:int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not Found")
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })

    db.commit()
    return "Updated Implemented"

def user_delete(db: Session, id:int):
    user = db.query(DbUser).filter(DbUser.id == id)
    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not Found")
    user.delete()
    db.commit()
    return "Delete Successful"





