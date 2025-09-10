from dotenv import load_dotenv
from os import getenv

PUBLIC_PATHS = ["/login", "/signup", "/docs", "/openapi.json", "/redoc"]

async def get_db_url():
    load_dotenv()
    return getenv("DATABASE_URL")

async def get_supabase_url():
    load_dotenv()
    return getenv("SUPABASE_URL")

async def get_supabase_key():
    load_dotenv()
    return getenv("SUPABASE_KEY")

async def get_api_key():
    load_dotenv()
    return getenv("API_KEY")

async def get_api_key_name():
    load_dotenv()
    return getenv("API_KEY_NAME")