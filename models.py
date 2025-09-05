from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id_user:str
    email:str
    password_hash:str
    profile_picture:Optional[str] = ""
    description:Optional[str] = ""
    followers_count:Optional[int] = 0
    following_count:Optional[int] = 0
    created:Optional[datetime] = datetime.now()

class Post(BaseModel):
    id_post:Optional[int]
    id_user:str
    contentPost:str
    likesCount:Optional[int]
    comments_count:Optional[int]
    created:Optional[datetime]

class Follows(BaseModel):
    id_user_follower:str
    id_user_following:str

class Replies(BaseModel):
    id_post:int
    id_reply:int

class Likes(BaseModel):
    id_post:int
    id_user:str