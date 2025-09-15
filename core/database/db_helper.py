from core.database.db_connection import get_pool
from asyncpg import Connection, Record
from typing import Optional

async def fetch_one(query:str, *params) -> Optional[Record] | None:
    pool = await get_pool()
    async with pool.acquire() as conn:
        conn:Connection
        return await conn.fetchrow(query, *params)

async def fetch_all(query:str, *params) -> list[Record]:
    pool = await get_pool()
    async with pool.acquire() as conn:
        conn:Connection
        return await conn.fetch(query, *params)

async def execute_query(query:str, *params) -> str:
    pool = await get_pool()
    async with pool.acquire() as conn:
        conn:Connection
        return await conn.execute(query, *params)