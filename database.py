import sqlite3
from datetime import datetime


def connect_db():
    return sqlite3.connect("users.db")


# Create table
def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY,
        first_name TEXT,
        username TEXT,
        joined_date TEXT
    )
    """)

    conn.commit()
    conn.close()

# get user 
def get_users():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT user_id, first_name, username, joined_date
    FROM users
    ORDER BY joined_date DESC
    """)

    users = cursor.fetchall()

    conn.close()

    return users

# Add user
def add_user(user_id, first_name, username):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO users
    (user_id, first_name, username, joined_date)
    VALUES (?, ?, ?, ?)
    """,
    (
        user_id,
        first_name,
        username,
        datetime.now().strftime("%Y-%m-%d")
    ))

    conn.commit()
    conn.close()


# Count users
def count_users():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")

    total = cursor.fetchone()[0]

    conn.close()

    return total