from fastapi import APIRouter
from fastapi import Response


router = APIRouter(prefix='/product', 
                   tags=['products']
                   )


products = ['watch', 'camera', 'phone']


@router.get('/all')
def get_all_product():
    data = " ".join(products)
    return Response(content=data, media_type="text/html")