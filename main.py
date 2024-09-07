from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional
from db import models
from db.database import engine
from router import blog_get
from router import blog_post
from router import user
from router import article

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(article.router)
app.include_router(blog_post.router)
app.include_router(user.router)


@app.get('/')
def index():
    return {"message": "Hello World"}


"""@app.get('/blog/all')
def index():
    return {"message": "All Blogs"}"""




models.Base.metadata.create_all(engine)