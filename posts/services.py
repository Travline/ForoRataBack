from posts.repository import insert_post
from utils.exceptions import ServiceError
from string import ascii_letters, digits
import random
from typing import Optional

async def generate_post_id() -> str:
  caracteres = ascii_letters + digits
  return ''.join(random.choice(caracteres) for _ in range(16))


async def create_post(content:str, user_id:str, reply:Optional[str]) -> bool:
  try:
    if not content:
      raise ServiceError("Missing post content")
    id_post: str = await generate_post_id()
    # if reply:
      # data = await insert_reply(id_post, content, user_id)
    data = await insert_post(id_post, content, user_id)
    if not data:
      raise ServiceError("Error creating post")
    return True
  except Exception as e:
    raise ServiceError(f"Creating post error {str(e)}") from e