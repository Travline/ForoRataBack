from users.models.schemas import UserProfileData, UserCreate
from users.repository import select_user_profile_data, insert_new_user
from utils.exceptions import ServiceError
from typing import Optional
from random import randint
from core.hash_managment import hash_secret
from asyncpg.exceptions import UniqueViolationError

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
            await insert_new_user(user_data)
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