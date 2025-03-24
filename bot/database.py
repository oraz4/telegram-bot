import psycopg2
from config import DATABASE_URL

conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

def add_user(user_id, name):
    cursor.execute("INSERT INTO users (user_id, name) VALUES (%s, %s) ON CONFLICT (user_id) DO NOTHING", (user_id, name))
    conn.commit()

def add_task(user_id, goal, duration, time_slot):
    cursor.execute("INSERT INTO tasks (user_id, goal, duration, time_slot) VALUES (%s, %s, %s, %s)", (user_id, goal, duration, time_slot))
    conn.commit()

def get_tasks(user_id):
    cursor.execute("SELECT goal, time_slot FROM tasks WHERE user_id = %s", (user_id,))
    return cursor.fetchall()
