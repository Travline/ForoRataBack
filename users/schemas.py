from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    id_user:str

class UserCreate(UserBase):
    email:EmailStr
    password_hash:str
    profile_picture:Optional[str] = ""

class UserSearchData(UserBase):
    profile_picture:str

class UserProfileData(UserSearchData):
    description:str
    followers:int
    following:int

class UserLogin(UserBase):
    password_hash:str
    