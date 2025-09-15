from asyncpg import Pool, create_pool
from core.config import get_db_url
from fastapi import FastAPI
from typing import Optional

pool: Optional[Pool] | None = None

async def connection_on():
    global pool
    pool = await create_pool(dsn=await get_db_url(), min_size=1, max_size=5)

async def connection_off():
    global pool
    if pool:
        await pool.close()

async def get_pool():
    if pool is None:
        raise RuntimeError("Database pool not initialized")
    return pool