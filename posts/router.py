from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from utils.exceptions import ServiceError
from typing import Optional
from core.middleware.jwt.jwt_protection import get_current_user
from posts.services import create_post

router = APIRouter()

@router.post("/add_post")
async def add_post(content:str, reply:Optional[str] , user_id:Optional[str] = Depends(get_current_user)):
  try:
    if user_id is None:
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing token")
    response = await create_post(content, user_id, reply)
    if not response:
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Post not created")
    return JSONResponse(content={"message": "Post created"}, status_code=status.HTTP_201_CREATED)
  except ServiceError as se:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")