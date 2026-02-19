from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import sqlite3
import uuid
import bcrypt
import config

router = APIRouter()

class UserRegister(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

def get_connection():
    return sqlite3.connect(config.DATABASE_NAME)

@router.post("/register")
def register(user: UserRegister):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (user.username,))
    if cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user.username, hashed_password))
    conn.commit()
    conn.close()
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: UserLogin):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (user.username,))
    db_user = cursor.fetchone()
    conn.close()

    if not db_user or not bcrypt.checkpw(user.password.encode("utf-8"), db_user[0]):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = str(uuid.uuid4())
    # ✅ Store in the shared config dictionary
    config.sessions[token] = user.username 
    return {"token": token}