from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PostRequest (BaseModel):
  content_post: str

class ReplyRquest (PostRequest):
  reply: str

class PostResponse (PostRequest):
  id_post: str
  id_user: str
  likes_count: int
  comments_count: int
  created: datetime