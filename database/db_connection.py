from psycopg2 import connect
import os
from dotenv import load_dotenv

def connection_on():
    load_dotenv()
    conn = connect(os.getenv("DATABASE_URL"))
    return conn