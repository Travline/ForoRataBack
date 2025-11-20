from typing import Optional, List
from core.database.db_helper import fetch_all, fetch_one
from asyncpg import PostgresError

async def basic_user_data(user_id:str) -> Optional[dict]:
  try:
    query = """SELECT profile_picture 
                FROM users WHERE id_user = $1;"""
    response = await fetch_one(query, user_id)
    if not response:
      return None
    data:dict = {"id_user":user_id}
    data.update(dict(response))
    return data
  except PostgresError as pe:
    raise PostgresError(pe)
  
async def verify_follows(follower:str, following:str) -> bool:
  try:
    query = """SELECT id_user_follower 
                FROM follows 
                WHERE id_user_following = $1 AND id_user_follower = $2;"""
    response = await fetch_one(query, following, follower)
    if not response:
      return False
    return True
  except PostgresError as pe:
    raise PostgresError(pe)