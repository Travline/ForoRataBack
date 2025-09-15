from fastapi import APIRouter, HTTPException, status
from users.models.schemas import UserCreate
from users.services import get_user_profile_data
from typing import Optional
from utils.exceptions import ServiceError

router = APIRouter()

@router.get("/profile_data_by_id/{user_id}")
async def get_profile_data(user_id:str) -> Optional[dict]:
    try:
        user = await get_user_profile_data(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except ServiceError as se:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
    
"""@router.post("/create_user")
async def create_user(user_data:UserCreate):
    return"""