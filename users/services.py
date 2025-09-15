from users.models.schemas import UserProfileData
from users.repository import select_user_profile_data
from utils.exceptions import ServiceError
from typing import Optional

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
    
"""async def creaate_user(user_data:UserCreate):
    try:    
        insert_new_user(user_data)
    except:
        return {"message":"Error"}"""