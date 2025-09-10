from fastapi import APIRouter

router = APIRouter()

@router.get("/posts")
async def get_home_posts(load_index:int):
    return

@router.post("/posts")
async def create_post(post):
    return

@router.get("/posts")
async def get_following_posts(user:str):
    return