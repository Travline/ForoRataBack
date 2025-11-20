from fastapi import Request, HTTPException, status, Response
from jose import jwt, JWTError
from datetime import datetime, UTC
from core.middleware.jwt.jwt_manager import create_token, read_token
from core.middleware.jwt.jwt_repository import findUser
from typing import Optional

async def get_current_user(request:Request) -> Optional[str]:
    token = request.cookies.get("fororata_access_token")
    if not token:
        return None
    try:
        payload = await read_token(token)
        user_exists = await findUser(payload.get("user_id"))
        if not user_exists:
            return None
        currentTime = int(datetime.now(UTC).timestamp())
        if (int(payload.get("exp")) < currentTime):
            return None
        return payload["user_id"]
    except JWTError:
        return None
    
async def send_cookie(cookie:Response, response:str):
    cookie.set_cookie(  
            key="fororata_access_token",
            value=response,
            httponly=True,
            samesite="none",
            secure=True
        )