from dotenv import load_dotenv
from os import getenv
from typing import Optional

PUBLIC_PATHS = ["/docs", "/openapi.json", "/redoc"]
NO_AUTH_PATHS = [""]

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

async def get_jwt_key() -> Optional[str]:
    load_dotenv()
    return getenv("JWT_KEY")

async def get_jwt_algorithm() -> Optional[str]:
    load_dotenv()
    return getenv("JWT_ALGORITHM")