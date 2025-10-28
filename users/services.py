from users.schemas import UserProfileData, UserCreate, UserLogin, UserSearchData
from users.repository import select_user_profile_data, insert_new_user, select_user_credentials, find_users
from utils.exceptions import ServiceError
from typing import Optional, List
from random import randint
from core.hash_manager import hash_secret, verify_secret
from asyncpg.exceptions import UniqueViolationError
from core.middleware.jwt.jwt_manager import create_token

async def random_rat_url():
    rats_url = ["https://umoiqpsvrnfyqgdzxcjm.supabase.co/storage/v1/object/public/rats/eat.webp",
                "https://umoiqpsvrnfyqgdzxcjm.supabase.co/storage/v1/object/public/rats/helm.webp",
                "https://umoiqpsvrnfyqgdzxcjm.supabase.co/storage/v1/object/public/rats/noc.webp",
                "https://umoiqpsvrnfyqgdzxcjm.supabase.co/storage/v1/object/public/rats/roasted.webp",
                "https://umoiqpsvrnfyqgdzxcjm.supabase.co/storage/v1/object/public/rats/roll.webp",
                "https://umoiqpsvrnfyqgdzxcjm.supabase.co/storage/v1/object/public/rats/snake.webp",
                "https://umoiqpsvrnfyqgdzxcjm.supabase.co/storage/v1/object/public/rats/xd.webp"]
    return rats_url[randint(0,6)] 

async def create_new_user(user_data:UserCreate):
    try:
        user_data.id_user = str(user_data.id_user.strip())
        if len(user_data.id_user) >= 2:
            user_data.password_hash = await hash_secret(user_data.password_hash)
            user_data.profile_picture = await random_rat_url()
            response = await insert_new_user(user_data)
            token = await create_token(response["id_user"])
            return token
        else:
            raise ServiceError(f"Creating user error in id_user")
    except UniqueViolationError as uve:
        raise UniqueViolationError(f"Creating user error: {str(uve)}") from uve

async def get_user_profile_data(user_id:str) -> Optional[dict]:
    try:
        data = await select_user_profile_data(user_id)
        if not data:
            return None
        user = UserProfileData(
            id_user=data["id_user"],
            profile_picture=data["profile_picture"],
            description=data["description"], #\n to <br>
            followers=data["followers_count"],
            following=data["following_count"]
        )
        return user.model_dump()
    except Exception as e:
        raise ServiceError(f"Building user error: {str(e)}") from e
    
async def check_user_login(user_data:UserLogin) -> Optional[dict]:
    try:
        data = await select_user_credentials(user_data.id_user.strip())
        if not data is None:
            storaged_pass = data["password_hash"]
            if await verify_secret(storaged_pass, user_data.password_hash.strip()):
                user = user_data.id_user.strip()
                token = await create_token(user)
                return token
    except Exception as e:
        raise ServiceError(f"Building user error: {str(e)}") from e
    
async def searching_user(user_id:str) -> Optional[List[dict]]:
    try:
        data = await find_users(user_id.strip())
        response:List[dict] = []
        for d in data:
            response.append(UserSearchData(id_user=d["id_user"],profile_picture=d["profile_picture"]).model_dump())
        return response
    except Exception as e:
        raise ServiceError(f"Building user error: {str(e)}") from e