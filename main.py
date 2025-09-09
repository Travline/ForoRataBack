from fastapi import FastAPI
from models import Post
from users.routes import users_router

app = FastAPI()

app.include_router(users_router.router)