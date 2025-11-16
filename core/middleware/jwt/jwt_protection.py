from fastapi import Request, HTTPException, status, Response
from jose import jwt, JWTError
from datetime import datetime, UTC
from core.middleware.jwt.jwt_manager import create_token, read_token
from core.middleware.jwt.jwt_repository import findUser
from typing import Optional

async def get_current_user(request:Request) -> Optional[str]:
    token = request.cookies.get("fororata_access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing JWT cookie")
    try:
        payload = await read_token(token)
        user_exists = await findUser(payload.get("user_id"))
        if not user_exists:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid user")
        currentTime = int(datetime.now(UTC).timestamp())
        if (int(payload.get("exp")) < currentTime):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Expired token")
        return payload["user_id"]
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid JWT")
    
async def send_cookie(cookie:Response, response:str):
    cookie.set_cookie(  
            key="fororata_access_token",
            value=response,
            httponly=True,
            samesite="lax",
            secure=False
        )