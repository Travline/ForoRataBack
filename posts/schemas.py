from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PostRequest (BaseModel):
  id_user: str
  content_post: str

class PostResponse (PostRequest):
  id_post: str
  likes_count: int
  comments_count: int
  created: datetime