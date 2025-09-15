from core.database.db_helper import fetch_one
from asyncpg.exceptions import PostgresError
from typing import Optional
from utils.exceptions import RepositoryError

async def select_user_profile_data(user_id:str) -> Optional[dict]:
    try:
        query = ("SELECT profile_picture, description, followers_count, following_count "+
                 "FROM users WHERE id_user = $1;")
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
    
"""async def insert_new_user(user_data:UserCreate):
    try:
        conn = await connection_on()
        cur = conn.cursor()
        cur.execute(INSERT INTO users(id_user, email, password_hash, profile_picture) 
                    VALUES (%s, %s, %s, %s);,
                    (user_data.id_user,
                     user_data.email,
                     user_data.password_hash,
                     user_data.profile_picture))
        conn.commit()
        cur.close()
        conn.close()
        return {"message":"Created"}
    except Error as e:
        return {"message":str(e.pgerror)}"""