from fastapi import FastAPI, HTTPException

from .schemas import PostCreate

app = FastAPI()

text_post={
            1:{"title":"new post","content":"brooo"},
            2:{"title":"2 post", "content":"hello world" },
            3:{"title":"3 post", "content":"my first post"},
            4:{"title":"4 post", "content":"fastapi is great"},
            5:{"title":"5 post", "content":"I love programming"},
            6:{"title":"6 post", "content":"lets build something awesome"},
        }

@app.get("/posts")
def post():
    return text_post

@app.get("/posts/{id}")
def get_post(id:int):
    if id not in text_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_post.get(id, {"message":"post not found"})

@app.get("/fposts/")
def filter(c_type: str, limit : int = None ):
    filtered=[]
    j= 0 if c_type =="e" else 1
    for i in text_post.keys():
        if i%2 == j:
            if (limit != None)  and limit >=1:
                limit -=1
                filtered.append(text_post[i])
            elif (limit== None):
                filtered.append(text_post[i])
    return filtered


@app.post("/posts/")
def create(post :PostCreate )-> PostCreate:
    text_post[max(text_post.keys())+1]=post
    return text_post[max(text_post.keys())]