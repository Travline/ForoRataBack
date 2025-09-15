from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.database.db_connection import connection_on, connection_off
from users.routes.router import router as users_router

@asynccontextmanager
async def lifespan(app:FastAPI):
    await connection_on()
    yield
    await connection_off()

app = FastAPI(lifespan=lifespan)

app.include_router(users_router, prefix="/users")