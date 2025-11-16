from posts.repository import insert_post
from utils.exceptions import ServiceError
from string import ascii_letters, digits
import random

async def generate_post_id() -> str:
  caracteres = ascii_letters + digits
  return ''.join(random.choice(caracteres) for _ in range(16))


async def create_post(content:str, user_id:str, reply:str) -> bool:
  try:
    if not content:
      raise ServiceError("Missing post content")
    id_post: str = await generate_post_id()
    data = await insert_post(id_post, content, user_id)
    if not data:
      raise ServiceError("Error creating post")
  except Exception as e:
    raise ServiceError(f"Creating post error {str(e)}") from e