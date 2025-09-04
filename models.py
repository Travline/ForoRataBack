from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id_user:str
    email:str
    password_hash:str
    profile_picture:str
    description:str
    followers_count:str
    following_count:str
    created:datetime

class Post(BaseModel):
    id_post:int
    id_user:str
    contentPost:str
    likesCount:int
    comments_count:int
    created:datetime

class Follows(BaseModel):
    id_user_follower:str
    id_user_following:str

class Replies(BaseModel):
    id_post:int
    id_reply:int

class Likes(BaseModel):
    id_post:int
    id_user:str