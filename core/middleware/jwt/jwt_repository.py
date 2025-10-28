from asyncpg import PostgresError
from core.database.db_helper import fetch_one

async def findUser(user_id:str) -> bool:
    try:
        query = "SELECT id_user from users WHERE id_user = $1"
        response = await fetch_one(query, user_id)
        if not response:
            return False
        return True
    except PostgresError as pe:
        raise PostgresError(str(pe)) from pe
