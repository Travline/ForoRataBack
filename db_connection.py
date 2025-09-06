import psycopg2
import os
from dotenv import load_dotenv


def connection_on():
    load_dotenv()
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    return conn
   