from fastapi import FastAPI
from db_connection import connection_on

app = FastAPI()

@app.get("/")
async def test():
    con = await connection_on()
    cur = con.cursor()
    cur.execute("Select * FROM users;")
    response = cur.fetchall()
    con.close()
    cur.close()
    return {"rsp":str(response)}
    