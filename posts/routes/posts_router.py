from fastapi import APIRouter
from database.db_connection import connection_on
from models import User
from psycopg2 import Error

router = APIRouter()

@router.get("/posts")
async def get_home_posts(load_index:int):
    return

@router.post("/posts")
async def create_post(post:Post):
    return

@router.get("/posts")
async def get_following_posts(user:str):
    return