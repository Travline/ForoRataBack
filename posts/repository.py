from core.database.db_helper import execute_query, fetch_all
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
  
async def select_home_posts() -> Optional[List[PostResponse]]:
  try:
    query = """SELECT content_post, id_post, id_user, likes_count, comments_count, created FROM posts"""
    data = await fetch_all(query)
    print(data)
    if not data:
      return None
    res:List[PostResponse] = []
    for post in data:
      res.append(PostResponse(
        content_post=post["content_post"],
        id_post=post["id_post"],
        id_user=post["id_user"],
        likes_count=post["likes_count"],
        comments_count=post["comments_count"],
        created=post["created"]
      ))
    return res
  except PostgresError as pge:
    print(str(pge))
    raise PostgresError(f"{str(pge)}") from pge