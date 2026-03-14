import sqlite3
import json
import os

class FeedbackLoop:
    def __init__(self, db_path="data/portfolio.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS proposals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_description TEXT,
                draft TEXT,
                status TEXT DEFAULT 'Draft', -- Draft, Sent, Won, Lost
                performance_notes TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        conn.close()

    def save_proposal(self, job_desc, draft):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO proposals (job_description, draft) VALUES (?, ?)",
            (job_desc, draft)
        )
        conn.commit()
        last_id = cursor.lastrowid
        conn.close()
        return last_id

    def update_status(self, proposal_id, status, notes=""):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE proposals SET status = ?, performance_notes = ? WHERE id = ?",
            (status, notes, proposal_id)
        )
        conn.commit()
        conn.close()

    def get_winning_examples(self, limit=3):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT job_description, draft FROM proposals WHERE status = 'Won' ORDER BY timestamp DESC LIMIT ?",
            (limit,)
        )
        examples = [{"job": r[0], "proposal": r[1]} for r in cursor.fetchall()]
        conn.close()
        return examples
