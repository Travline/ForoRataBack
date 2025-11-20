from posts.repository import insert_post, select_home_posts
from utils.exceptions import ServiceError
from string import ascii_letters, digits
import random
from typing import Optional, List
from posts.schemas import PostResponse

async def generate_post_id() -> str:
  caracteres = ascii_letters + digits
  return ''.join(random.choice(caracteres) for _ in range(16))


async def create_post(content:str, user_id:str) -> bool:
  try:
    if not content:
      raise ServiceError("Missing post content")
    id_post: str = await generate_post_id()
    # if reply != '':
      # data = await insert_reply(id_post, content, user_id)
    data = await insert_post(id_post, content, user_id)
    if not data:
      raise ServiceError("Error creating post")
    return True
  except Exception as e:
    raise ServiceError(f"Creating post error {str(e)}") from e
  
async def get_home_posts() -> Optional[List[PostResponse]]:
  try:
    data = await select_home_posts()
    print(data)
    if not data:
      return None
    return data
  except Exception as e:
      print(e)
      raise ServiceError(f"Building user error: {str(e)}") from e