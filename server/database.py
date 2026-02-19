import sqlite3
from datetime import datetime
import config

def get_connection():
    conn = sqlite3.connect(
        config.DATABASE_NAME,
        check_same_thread=False,
        timeout=10
    )
    # This allows us to access columns by name: row['username']
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        message TEXT NOT NULL,
        timestamp TEXT NOT NULL
    )""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )""")
    conn.commit()
    conn.close()

def save_message(username, message):
    conn = get_connection()
    cursor = conn.cursor()
    ts = datetime.now().strftime("%H:%M:%S")
    cursor.execute("INSERT INTO messages(username, message, timestamp) VALUES (?, ?, ?)", 
                   (username, message, ts))
    conn.commit()
    conn.close()

def get_chat_history(limit=20):
    conn = get_connection()
    cursor = conn.cursor()
    # Fetching history
    cursor.execute("SELECT username, message, timestamp FROM messages ORDER BY id DESC LIMIT ?", (limit,))
    rows = cursor.fetchall()
    conn.close()
    
    # Convert SQLite Rows to a list of real dictionaries to prevent crashes
    history = [{"username": r["username"], "message": r["message"], "timestamp": r["timestamp"]} for r in rows]
    return history[::-1]