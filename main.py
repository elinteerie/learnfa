from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

from router import blog_get
from router import blog_post

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get('/')
def index():
    return {"message": "Hello World"}


"""@app.get('/blog/all')
def index():
    return {"message": "All Blogs"}"""


