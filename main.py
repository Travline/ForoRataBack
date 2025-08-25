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
    for i in [1, 2, 3]:    
        response = (cur.fetchone())[i]
        return {"rsp":str(response)}