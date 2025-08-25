from fastapi import FastAPI
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

async def connectiondb():
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    return conn.cursor()

app = FastAPI()

@app.get("/")
async def test():
    cur = await connectiondb()
    cur.execute("Select * FROM users;")
    response = (cur.fetchone())[1]
    return {"email":str(response)}