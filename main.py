from fastapi import FastAPI
from psycopg2 import Error
from db_connection import connection_on
from models import User
from typing import List

app = FastAPI()

@app.post("/users")
async def create_new_user(user:User):
    try:    
        conn = connection_on()
        cur = conn.cursor()
        cur.execute("""INSERT INTO users(id_user, email, password_hash, profile_picture) 
                       VALUES (%s, %s, %s, %s);""",
                    (user.id_user, user.email, user.password_hash, user.profile_picture,))
        conn.commit()
        cur.close()
        conn.close()
        return {"message":True}
    except Error as e:
        return {"message":str(e.pgerror)}


@app.get("/users/{user_id}")
async def get_user_data(user_id:str):
    try:    
        conn = connection_on()
        cur = conn.cursor()
        cur.execute("""SELECT id_user, email, password_hash, profile_picture, description, followers_count, following_count, created 
                       FROM users WHERE id_user = %s;""", (user_id,))
        response = cur.fetchone()
        user = User(
            id_user= response[0],
            email = response[1],
            password_hash = response[2],
            profile_picture = response[3],
            description = response[4],
            followers_count = response[5],
            following_count = response[6],
            created = response[7],
        )
        cur.close()
        conn.close()
        return user.model_dump()
    except Error as e:
        return {"message":str(e.pgerror)}