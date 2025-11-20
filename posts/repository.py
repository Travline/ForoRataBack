from core.database.db_helper import execute_query, fetch_all, fetch_one
from asyncpg import UniqueViolationError, PostgresError
from posts.schemas import PostResponse
from typing import Optional, List

async def insert_post(id_post:str, content:str, user_id:str) -> bool:
  try:
    query = """INSERT INTO posts (id_post, content_post, id_user) 
                VALUES($1, $2, $3);"""
    await execute_query(query, id_post, content, user_id)
    return True
  except UniqueViolationError as uve:
      raise UniqueViolationError(f"{str(uve)}") from uve
  
async def select_home_posts() -> Optional[List[dict]]:
  try:
    query = """SELECT content_post, id_post, id_user, likes_count, comments_count, created FROM posts"""
    data = await fetch_all(query)
    if not data:
      return None
    response: List[dict] = []
    for d in data:
      response.append(dict(d))
    return response
  except PostgresError as pge:
    print(str(pge))
    raise PostgresError(f"{str(pge)}") from pge
  
async def verify_likes(id_user:str, id_post:str) -> bool:
  try:
    query = """SELECT id_user 
                FROM likes 
                WHERE id_user = $1 AND id_post = $2;"""
    response = await fetch_one(query, id_user, id_post)
    if not response:
      return False
    return True
  except PostgresError as pe:
    raise PostgresError(pe)
  
async def count_likes(id_post:str) -> int:
  try:
    query = """SELECT id_user FROM likes WHERE id_post = $1"""
    data = await fetch_all(query, id_post)
    if not data:
      return 0
    response: List[dict] = []
    for d in data:
      response.append(dict(d))
    return len(response)
  except PostgresError as pge:
    print(str(pge))
    raise PostgresError(f"{str(pge)}") from pge
  
async def count_replies(id_post:str) -> int:
  try:
    query = """SELECT id_reply FROM replies WHERE id_post = $1"""
    data = await fetch_all(query, id_post)
    if not data:
      return 0
    response: List[dict] = []
    for d in data:
      response.append(dict(d))
    return len(response)
  except PostgresError as pge:
    print(str(pge))
    raise PostgresError(f"{str(pge)}") from pge