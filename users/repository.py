from core.database.db_helper import fetch_one, execute_query
from asyncpg.exceptions import PostgresError, UniqueViolationError
from typing import Optional
from utils.exceptions import RepositoryError
from users.models.schemas import UserCreate, UserLogin

async def select_user_profile_data(user_id:str) -> Optional[dict]:
    try:
        query = """SELECT profile_picture, description, followers_count, following_count 
                    FROM users WHERE id_user = $1;"""
        response = await fetch_one(query, user_id)
        if not response:
            return None
        data = dict(
            id_user = user_id,
            profile_picture = response["profile_picture"],
            description = response["description"],
            followers_count = response["followers_count"],
            following_count = response["following_count"]
        )
        return data
    except PostgresError as pe:
        raise RepositoryError(f"DB error with select_user_profile_data '{user_id}': {str(pe)}") from pe
    
async def insert_new_user(user_data:UserCreate) -> Optional[str]:
    try:
        query = """INSERT INTO users (id_user, email, password_hash, profile_picture) 
                    VALUES($1, $2, $3, $4);"""
        await execute_query(query,
                            user_data.id_user,
                            user_data.email,
                            user_data.password_hash,
                            user_data.profile_picture)
        data = await fetch_one("SELECT id_user FROM users WHERE id_user = $1",
                                   user_data.id_user)
        if not data is None:
            return {"id_user":data["id_user"]}
    except UniqueViolationError as uve:
        raise UniqueViolationError(f"{str(uve)}") from uve
    
async def select_user_credentials(user_id:str) -> Optional[str]:
    try:
        query = """SELECT password_hash FROM users 
                   WHERE id_user = $1"""
        response = await fetch_one(query, user_id)
        return {"password_hash":response["password_hash"]}
    except PostgresError as pe:
        raise RepositoryError(f"DB error with select_user_profile_data : {str(pe)}") from pe