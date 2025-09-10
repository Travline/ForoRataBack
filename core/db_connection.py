from psycopg2 import connect
from core.config import get_db_url, get_supabase_key, get_supabase_url
from supabase import create_client, Client

async def supabase_on():
    supabase:Client = create_client(supabase_url= await get_supabase_url,
                                          supabase_key=await get_supabase_key)
    return supabase

async def connection_on():
    conn = connect(await get_db_url())
    return conn