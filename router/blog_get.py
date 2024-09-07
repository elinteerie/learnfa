from fastapi import APIRouter
from enum import Enum
from typing import Optional
from fastapi import status, Response, Depends
from .blog_post import required_functionality

router = APIRouter(prefix='/blog', 
                   tags=['blog']
                   )


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@router.get('/type/{type}', 
         
         summary="Retrieve A Post Type",
         description="Please Follow",
         response_description="omo"
         )
def blog_type(type: BlogType):
    return {'message': f"THis is a type of {type.value}"}


@router.get('/all/')
def blog_type(page: int =1, page_size: Optional[int]= None, req_parameter: dict = Depends(required_functionality)):
    return {'message': f"THis is a type of {page} and size of {page_size}", "req": req_parameter}



@router.get('/{id}', status_code=status.HTTP_404_NOT_FOUND)
def indexblog(id: int, response: Response):
    if id > 5:
        return {"error": f"blog with this id {id} not found"}
        
    else: 
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog with {id}"}







