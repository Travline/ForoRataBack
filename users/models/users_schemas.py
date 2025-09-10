from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserRequest(BaseModel):
    id_user:str
    email:str
    password_hash:str
    profile_picture:Optional[str]
    description:Optional[str]
    followers_count:Optional[int]
    following_count:Optional[int]
    created:Optional[datetime]