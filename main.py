from fastapi import FastAPI
from db_connection import connection_on
from models import User
from typing import List

app = FastAPI()

@app.post("/user")
async def create_new_user(user:User):
    return user.model_dump()

@app.get("/user/{user}")
async def get_user_data():
    user:List = []
    con = await connection_on()
    cur = con.cursor()
    cur.execute("Select * FROM users;")
    response = cur.fetchall()
    con.close()
    cur.close()
    return {"rsp":str(response)}