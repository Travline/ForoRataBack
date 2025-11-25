from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class PostRequest (BaseModel):
  content_post: str
  reply_to: Optional[str]

class PostResponse (PostRequest):
  id_post: str
  id_user: str
  likes_count: int
  comments_count: int
  profile_picture: str
  followed: bool
  liked: bool
  created: str

class PostFocusResponse (PostResponse):
  replies: List[PostResponse]