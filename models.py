from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Follows(BaseModel):
    id_user_follower:str
    id_user_following:str

class Replies(BaseModel):
    id_post:int
    id_reply:int

class Likes(BaseModel):
    id_post:int
    id_user:str