from posts.repository import insert_post, select_home_posts, verify_likes, count_likes, count_replies
from utils.exceptions import ServiceError
from string import ascii_letters, digits
import random
from typing import Optional, List
from posts.schemas import PostResponse
from public.querys import basic_user_data, verify_follows
from utils.time import delta_between_dates

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
  
async def get_home_posts(id_user:str) -> Optional[List[PostResponse]]:
  try:
    data = await select_home_posts()
    if not data:
      return None
    res: List[PostResponse] = []
    following = False
    like = False
    if id_user != '':
      following = await verify_follows()
      like = await verify_likes()
    for post in data:
      pfp = await basic_user_data(post["id_user"])
      res.append(PostResponse(
        id_post=post["id_post"],
        id_user=post["id_user"],
        profile_picture= pfp["profile_picture"],
        content_post=post["content_post"],
        followed= following,
        liked= like,
        likes_count= await count_likes(post["id_post"]),
        comments_count= await count_replies(post["id_post"]),
        created= await delta_between_dates(post["created"])
      ))
    return res
  except Exception as e:
      print(e)
      raise ServiceError(f"Building user error: {str(e)}") from e