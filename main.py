from fastapi import FastAPI, Request, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from core.middleware.jwt.jwt_protection import get_current_user
from core.database.db_connection import connection_on, connection_off
from users.router import router as users_router
from posts.router import router as posts_router
from typing import Optional

@asynccontextmanager
async def lifespan(app:FastAPI):
    await connection_on()
    yield
    await connection_off()

app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:4200",
    "http://localhost:3000",
    "https://fororata.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router, prefix="/users")
app.include_router(posts_router, prefix="/posts")

@app.get("/me")
async def me(user_id:Optional[str] = Depends(get_current_user)):
    try:
        if user_id:
            return {"me" : user_id}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error: {str(e)}")