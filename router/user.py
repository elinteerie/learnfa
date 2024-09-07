from fastapi import APIRouter
from schemas import UserBase, UserDisplay
from db.db_user import create_user
from fastapi import Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from typing import List

router = APIRouter(prefix='/user', 
                   tags=['users']
                   )


#Create User

@router.post('/', response_model=UserDisplay)
def create_users(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


#Read All User
@router.get('/all', response_model=List[UserDisplay])
def get_all_users(db: Session= Depends(get_db)):
    return db_user.get_all_users_a(db)


#Read One User
@router.get('/{id}', response_model=UserDisplay)
def get_userid(id: int, db: Session= Depends(get_db)):
    return db_user.get_user_by_id(db, id)



#Update User
@router.post('/{id}/update')
def update_user(id: int, request:UserBase,  db: Session=Depends(get_db)):
    return db_user.update_user(db, id, request)



@router.post('/{id}/delete')
def user_delete(id: int, db: Session=Depends(get_db)):
    return db_user.user_delete(db, id)

