from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Post(BaseModel):
    id_post:Optional[int]
    id_user:str
    contentPost:str
    likesCount:Optional[int]
    comments_count:Optional[int]
    liked:Optional[bool]
    created:Optional[datetime]