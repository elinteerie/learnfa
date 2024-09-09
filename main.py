from fastapi import FastAPI, status, Response, Request, HTTPException
from enum import Enum
from typing import Optional
from db import models
from db.database import engine
from router import blog_get
from router import blog_post
from router import file
from router import user
from router import article
from auth import authentication
from router import product
from router import dependencies
from exceptions import StoryException
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import time
import websockets
from client import html
from fastapi.websockets import WebSocket


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(article.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(product.router)
app.include_router(authentication.router)
app.include_router(file.router)
app.include_router(dependencies.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




"""@app.get('/')
def index():
    return {"message": "Hello World"}"""


"""@app.get('/blog/all')
def index():
    return {"message": "All Blogs"}"""


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418, 
        content={'detail': exc.name}
    )


@app.get("/")
async def get():
    return HTMLResponse(html)


#websockets
clients = []

"""@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    while True:
        data = await websocket.receive_text()
        for client in clients:
            await client.send_text(data)
"""



@app.middleware('http')
async def add_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    response.headers['duration'] =str(duration)
    return response


"""
@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return PlainTextResponse(
        str(exc), status_code=400
       
    )
"""
models.Base.metadata.create_all(engine)

app.mount('/files', StaticFiles(directory='files'), name='files' )


