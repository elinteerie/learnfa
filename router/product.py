from fastapi import APIRouter
from fastapi import Response, Header, Cookie, Form
from fastapi.responses import HTMLResponse
from typing import Optional


router = APIRouter(prefix='/product', 
                   tags=['products']
                   )


products = ['watch', 'camera', 'phone']

@router.post('/new')
def create_product(name:str =Form(...)):
    products.append(name)
    return products


@router.get('/withheader')
def get_prod(response: Response,
             custom_header: Optional[str]= Header(None),
             test_cookie: Optional[str]= Cookie(None)):
    
    
    
    
    return {
        "data": products,
        "custom_header": custom_header,
        "my_cooker": test_cookie

    }



@router.get('/all')
def get_all_product():
    data = " ".join(products)
    response =Response(content=data, media_type="text/plain")
    response.set_cookie("test_cookie", value="test_874766474")
    return response


@router.get('/{id}', responses={
    200:{
        "content":{
            "text/html":{
                "a htmk"
            }
        },
        "description": "Returns a Html"
    },

    404:{
        "content":{
            "text/plain":{
                "a htmk"
            }
        },
        "description": "Returns a Html"
    }

})
def get_product(id: int):
    product = products[id]
    out = """
    <head>
    <style>
    .product {{
    width: 500px;
    border: 2px inset green;
    }}
    </style>
    </head>
    <div class="product"> {product}</div>


    """
    return HTMLResponse(content=out, media_type='text/html')