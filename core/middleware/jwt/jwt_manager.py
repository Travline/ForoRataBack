from core.config import get_jwt_key, get_jwt_algorithm
from jose import jwt, JWTError
from datetime import datetime, UTC
from typing import Optional

async def create_token(user_id) -> Optional[str]:
    currentTime = int(datetime.now(UTC).timestamp())
    exp:int = currentTime + 3600
    payload:dict = {
        "user_id": user_id,
        "exp" : exp
    }
    try:
        token = jwt.encode(payload,
                        key= await get_jwt_key(),
                        algorithm= await get_jwt_algorithm())
        return token
    except JWTError as jwte:
        raise JWTError(jwte)

async def read_token(token:str) -> Optional[dict]:
    try:
        payload:dict = jwt.decode(token=token,
                                key= await get_jwt_key(),
                                algorithms= await get_jwt_algorithm())
        return payload
    except JWTError as jwte:
        print(jwte)
        raise JWTError(jwte)