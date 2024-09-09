from fastapi import APIRouter
from fastapi.requests import Request
from fastapi import Depends

router = APIRouter(prefix='/dependencies', tags=['dep'])


def convert_params(request: Request):
    out_param = []
    for k, v in request.query_params.items():
        out_param.append(f'{k}--{v}')
    return out_param

def convert_headers(request: Request, separator: str, query =Depends(convert_params)):
    out_headers = []
    for k, v in request.headers.items():
        out_headers.append(f"{k} {separator} {v}")
    return {
        "header": out_headers,
            "query": query    
            }
    

@router.get('')
def get_items(separator: str = "--",  headers = Depends(convert_headers)):
    return {
        "items": ['a', 'b', 'c'],
        "headers": [headers]
    }

class Account:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

@router.post('/user')
def create_user(name: str, email: str, password: str, account: Account = Depends()):
    
    return {
        "name": account.name,
        "email": account.email

    }
        
