from fastapi import FastAPI
from db_connection import connection_on

app = FastAPI()

@app.get("/users")
async def get_posts():
    con = await connection_on()
    cur = con.cursor()
    cur.execute("Select * FROM users;")
    response = cur.fetchall()
    con.close()
    cur.close()
    return {"rsp":str(response)}