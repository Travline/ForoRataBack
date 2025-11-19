from fastapi import APIRouter, HTTPException, status, Request, Response
from fastapi.responses import JSONResponse
from users.schemas import UserCreate, UserLogin, UserSearchData
from users.services import get_user_profile_data, create_new_user, check_user_login, searching_user
from typing import Optional, List
from utils.exceptions import ServiceError
from asyncpg.exceptions import UniqueViolationError
from core.middleware.jwt.jwt_protection import send_cookie

router = APIRouter()

@router.get("/profile_data/{user_id}")
async def get_profile_data(user_id:str) -> Optional[dict]:
    try:
        user = await get_user_profile_data(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user
    except ServiceError as se:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
    
@router.post("/register")
async def create_user(cookie:Response, user_data:UserCreate):
    try:
        response = await create_new_user(user_data)
        if not response is None:
            send_cookie(cookie, response)
            return JSONResponse(content=response, status_code=status.HTTP_201_CREATED)
    except UniqueViolationError as uve:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User alredy exists")
    except ServiceError as se:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.post("/login")
async def user_login(cookie:Response,user_data:UserLogin):
    try:
        response = await check_user_login(user_data)
        if not response:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        await send_cookie(cookie, response)
        return { "message": "Loged successfully" }
    except ServiceError as se:
        print(se)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.get("/searching")
async def user_searching(user_id:str) -> Optional[List[dict]]:
    try:
        response = await searching_user(user_id.strip())
        if not response:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return response
    except ServiceError as se:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")