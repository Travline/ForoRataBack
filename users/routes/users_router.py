from fastapi import APIRouter
from database.db_connection import connection_on
from models.user_request import UserRequest
from psycopg2 import Error

router = APIRouter()

@router.get("/users/{user_id}")
async def get_user_data(user_id:str):
    try:    
        conn = connection_on()
        cur = conn.cursor()
        cur.execute("""SELECT id_user, profile_picture, description, followers_count, following_count 
                       FROM users WHERE id_user = %s;""", (user_id,))
        response = cur.fetchone()
        user = UserRequest()
        user.id_user = response[0]
        user.profile_picture = response[1]
        user.description = response[2]
        user.followers_count = response[3]
        user.following_count = response[4]
        cur.close()
        conn.close()
        return {"id_user":user.id_user,
                "profile_picture":user.profile_picture,
                "description":user.description,
                "followers_count":user.followers_count,
                "following_count":user.following_count
                }
    except Error as e:
        return {"message":str(e.pgerror)}
    
@router.post("/users")
async def create_user(user:UserRequest):
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