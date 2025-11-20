from core.database.db_helper import execute_query
from asyncpg import UniqueViolationError

async def insert_post(id_post:str, content:str, user_id:str) -> bool:
  try:
    query = """INSERT INTO posts (id_post, content, id_user) 
                VALUES($1, $2, $3);"""
    await execute_query(query, id_post, content, user_id)
    return True
  except UniqueViolationError as uve:
      raise UniqueViolationError(f"{str(uve)}") from uve