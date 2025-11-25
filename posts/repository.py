from core.database.db_helper import execute_query, fetch_all, fetch_one
from asyncpg import UniqueViolationError, PostgresError
from posts.schemas import PostResponse, PostRequest
from typing import Optional, List

async def insert_post(id_post:str, post:PostRequest, user_id:str) -> bool:
  try:
    query = """INSERT INTO posts (id_post, content_post, reply_to, id_user) 
                VALUES($1, $2, $3, $4);"""
    await execute_query(query, id_post, post.content_post, post.reply_to, user_id)
    if post.reply_to:
      await execute_query("UPDATE posts SET comments_count = comments_count + 1 WHERE id_post = $1", post.reply_to)
      
    return True
  except UniqueViolationError as uve:
      raise UniqueViolationError(f"{str(uve)}") from uve
  
async def select_home_posts() -> Optional[List[dict]]:
  try:
    query = """SELECT id_post, id_user, reply_to, content_post, likes_count, comments_count, created
               FROM posts WHERE reply_to IS NULL ORDER BY created DESC"""
    data = await fetch_all(query)
    if not data:
      return None
    response: List[dict] = []
    for d in data:
      response.append(dict(d))
    return response
  except PostgresError as pge:
    raise PostgresError(f"{str(pge)}") from pge

async def select_replies(reply_to:str) -> Optional[List[dict]]:
  try:
    query = """SELECT id_post, id_user, reply_to, content_post, likes_count, comments_count, created
               FROM posts WHERE reply_to = $1 ORDER BY created DESC"""
    data = await fetch_all(query, reply_to)
    if not data:
      return None
    response: List[dict] = []
    for d in data:
      response.append(dict(d))
    return response
  except PostgresError as pge:
    raise PostgresError(f"{str(pge)}") from pge
  
async def select_focus_post(id_post_req) -> Optional[dict] :
  try:
    query = """SELECT content_post, id_post, id_user, reply_to, likes_count, comments_count, created 
                FROM posts WHERE id_post = $1"""
    data = await fetch_one(query, id_post_req)
    if not data:
      return None
    return dict(data)
  except PostgresError as pge:
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