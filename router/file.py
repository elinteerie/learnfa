from fastapi import APIRouter
from fastapi import File
from fastapi.responses import FileResponse

router = APIRouter(prefix='/file', tags=['file'])


@router.post('')
def get_file(file: bytes =File(...)):
    content = file.decode('utf-8')
    lines = content.split('\n')
    return {"lines": lines}


@router.get('download/{name}', response_class=FileResponse)
def get_file(name: str):
    path = f"files/{name}"
    return path


