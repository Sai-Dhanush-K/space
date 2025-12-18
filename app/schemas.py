from pydantic import BaseModel

class PostCreate(BaseModel):
    title : str
    caption : str