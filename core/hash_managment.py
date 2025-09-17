from argon2 import PasswordHasher
from argon2.exceptions import Argon2Error
from core.config import get_pepper
from typing import Optional
from utils.exceptions import HashError, VerifyHashError

ph = PasswordHasher(
    time_cost=2,
    memory_cost=32768,
    parallelism=1,
    hash_len=64,
    salt_len=16,
)

async def hash_secret(secret:str) -> Optional[str]:
    try:
        if len((str(secret)).strip()) >= 8:
            pepper =  await get_pepper()
            return ph.hash(secret+pepper)
        else:
            return None
    except Argon2Error as ae:
        raise HashError(f"Hashing error: {str(ae)}") from ae

async def verify_secret(storaged_secret:str, secret:str) -> Optional[bool]:
    try:
        if len((str(secret)).strip()) >= 8:
            return ph.verify(storaged_secret, secret+get_pepper())
        else:
            return None
    except Argon2Error as ae:
        raise VerifyHashError(f"Verify error: {str(ae)}") from ae