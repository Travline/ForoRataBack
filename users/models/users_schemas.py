from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    id_user:str

class UserCreate(UserBase):
    email:str
    password_hash:str
    profile_picture:Optional[str]

class UserFullData(UserBase):
    email:str
    profile_picture:Optional[str]