from dotenv import load_dotenv
from os import getenv
from typing import Optional

PUBLIC_PATHS = ["/login", "/signup", "/docs", "/openapi.json", "/redoc"]

async def get_db_url() -> Optional[str]:
    load_dotenv()
    return getenv("DATABASE_URL")

async def get_api_key() -> Optional[str]:
    load_dotenv()
    return getenv("API_KEY")

async def get_api_key_name() -> Optional[str]:
    load_dotenv()
    return getenv("API_KEY_NAME")

async def get_pepper() -> Optional[str]:
    load_dotenv()
    return getenv("PEPPER")