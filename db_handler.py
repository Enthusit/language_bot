import sqlite3
from datetime import datetime
import os

class DatabaseHandler:
    def __init__(self, db_path="/Users/basiljoy/my_project/LANGUAGE/language_bot/language_learning.db"):
        self.db_path = db_path
        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute('''
                CREATE TABLE IF NOT EXISTS learning_sessions (
                    id INTEGER PRIMARY KEY,
                    language TEXT,
                    level TEXT,
                    timestamp DATETIME
                )
            ''')
            c.execute('''
                CREATE TABLE IF NOT EXISTS conversations (
                    id INTEGER PRIMARY KEY,
                    session_id INTEGER,
                    user_input TEXT,
                    bot_response TEXT,
                    timestamp DATETIME,
                    FOREIGN KEY (session_id) REFERENCES learning_sessions(id)
                )
            ''')
            conn.commit()

    def create_session(self, language, level):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute(
                "INSERT INTO learning_sessions (language, level, timestamp) VALUES (?, ?, ?)",
                (language, level, datetime.now())
            )
            conn.commit()
            return c.lastrowid

    def save_conversation(self, session_id, user_input, bot_response):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute(
                "INSERT INTO conversations (session_id, user_input, bot_response, timestamp) VALUES (?, ?, ?, ?)",
                (session_id, user_input, bot_response, datetime.now())
            )
            conn.commit()