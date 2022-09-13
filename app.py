from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text , Optional
from datetime import datetime


app= FastAPI()

posts= []

# Post Model

class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at : datetime = datetime.now()
    published_at: Optional[datetime] 
    published: bool =False 

@app.get('/inicio')
def read_root():
    return {"Welcome":"Welcome to my API"}

@app.get('/posts')
def get_post():
    return posts

@app.post('/posts')
def save_post(post:Post):
    print(post.dict())
    return "recibido!"