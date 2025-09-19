from fastapi import APIRouter, HTTPException, status
from users.models.schemas import UserCreate, UserLogin
from users.services import get_user_profile_data, create_new_user, check_user_login
from typing import Optional
from utils.exceptions import ServiceError
from asyncpg.exceptions import UniqueViolationError

router = APIRouter()

@router.get("/profile_data_by_id/{user_id}")
async def get_profile_data(user_id:str) -> Optional[dict]:
    try:
        user = await get_user_profile_data(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user
    except ServiceError as se:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
    
@router.post("/register")
async def create_user(user_data:UserCreate):
    try:
        response = await create_new_user(user_data)
        if not response is None:
            return response
    except UniqueViolationError as uve:
        raise HTTPException(status_code=666, detail="User alredy exists")
    except ServiceError as se:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.post("/login")
async def user_login(user_data:UserLogin):
    try:
        response = await check_user_login(user_data)
        if not response:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        else:
            return response
    except ServiceError as se:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")