from posts.repository import insert_post, select_home_posts, verify_likes, select_focus_post, select_post_replies
from utils.exceptions import ServiceError
from string import ascii_letters, digits
import random
from typing import Optional, List
from posts.schemas import PostResponse, PostFocusResponse, PostRequest
from public.querys import basic_user_data, verify_follows
from utils.time import delta_between_dates

async def generate_post_id() -> str:
  caracteres = ascii_letters + digits
  return ''.join(random.choice(caracteres) for _ in range(16))


async def create_post(post:PostRequest, user_id:str) -> bool:
  try:
    if not post.content_post:
      raise ServiceError("Missing post content")
    id_post: str = await generate_post_id()
    data = await insert_post(id_post, post, user_id)
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
    
    for post in data:
      if id_user != '':
        following = await verify_follows(id_user, post["id_user"])
    
      like = await verify_likes(id_user, post["id_post"])
      pfp = await basic_user_data(post["id_user"])

      res.append(PostResponse(
        id_post=post["id_post"],
        id_user=post["id_user"],
        reply_to=post["reply_to"],
        profile_picture= pfp["profile_picture"],
        content_post=post["content_post"],
        followed= following,
        liked= like,
        likes_count= post["likes_count"],
        comments_count= post["comments_count"],
        created= await delta_between_dates(post["created"])
      ))
    return res
  except Exception as e:
      print(e)
      raise ServiceError(f"Building user error: {str(e)}") from e

async def set_replies(data:List[dict], id_user:str) -> List[PostResponse]:
  replies: List[PostResponse] = []
  
  if not data:
    return replies

  for post in data:
    following = False
    like = False
    
    if id_user != '':
      following = await verify_follows(id_user, post["id_user"])

    like = await verify_likes(id_user, post["id_post"])
    pfp = await basic_user_data(post["id_user"])
    
    replies.append(PostResponse(
      id_post=post["id_post"],
      id_user=post["id_user"],
      profile_picture= pfp["profile_picture"],
      content_post=post["content_post"],
      followed= following,
      liked= like,
      likes_count= post["likes_count"],
      comments_count= post["comments_count"],
      created= await delta_between_dates(post["created"])
    ))

  return replies

async def get_focus_post(id_post_req, id_user:str) -> Optional[PostFocusResponse]:
  try:
    post = await select_focus_post(id_post_req)
    if not post:
      return None
    
    following = False
    like = False
    
    if id_user != '':
      following = await verify_follows(id_user, post["id_user"])
  
    like = await verify_likes(id_user, post["id_post"])
    pfp = await basic_user_data(post["id_user"])
    data = await select_post_replies(post["id_post"])

    res = PostFocusResponse(
      id_post=post["id_post"],
      id_user=post["id_user"],
      profile_picture= pfp["profile_picture"],
      content_post=post["content_post"],
      followed= following,
      liked= like,
      likes_count= post["likes_count"],
      comments_count= post["comments_count"],
      created= await delta_between_dates(post["created"]),
      replies= await set_replies(data, id_user)
    )
    return res
  except Exception as e:
      raise ServiceError(f"Building user error: {str(e)}") from e