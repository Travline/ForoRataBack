import psycopg2
import os
from dotenv import load_dotenv


async def connection_on():
    load_dotenv()
    con = psycopg2.connect(os.getenv("DATABASE_URL"))
    return con
   