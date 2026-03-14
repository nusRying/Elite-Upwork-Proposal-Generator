import os
from typing import List
import fitz  # pymupdf
from docx import Document
import sqlite3
import json

class KnowledgeVault:
    def __init__(self, db_path="data/portfolio.db", knowledge_dir="data/knowledge"):
        self.db_path = db_path
        self.knowledge_dir = knowledge_dir
        os.makedirs(self.knowledge_dir, exist_ok=True)
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS knowledge_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT,
                content TEXT,
                metadata TEXT
            )
        """)
        conn.commit()
        conn.close()

    def ingest_file(self, file_path: str):
        filename = os.path.basename(file_path)
        ext = os.path.splitext(filename)[1].lower()
        
        content = ""
        if ext == ".pdf":
            doc = fitz.open(file_path)
            for page in doc:
                content += page.get_text() + "\n"
            doc.close()
        elif ext == ".docx":
            doc = Document(file_path)
            for para in doc.paragraphs:
                content += para.text + "\n"
        elif ext == ".txt":
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        else:
            raise ValueError(f"Unsupported file type: {ext}")

        # Store in DB
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO knowledge_items (filename, content, metadata) VALUES (?, ?, ?)",
            (filename, content, json.dumps({"source": file_path}))
        )
        conn.commit()
        conn.close()
        return filename

    def get_all_knowledge(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, filename, content, metadata FROM knowledge_items")
        items = [{"id": r[0], "filename": r[1], "snippet": r[2][:500], "content": r[2]} for r in cursor.fetchall()]
        conn.close()
        return items

    def search_knowledge(self, query: str, limit: int = 5):
        """Simple keyword search across full content."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        # Search in content using LIKE
        cursor.execute(
            "SELECT id, filename, content FROM knowledge_items WHERE content LIKE ?",
            (f"%{query}%",)
        )
        results = [{"id": r[0], "filename": r[1], "content": r[2]} for r in cursor.fetchall()]
        conn.close()
        return results[:limit]

    def delete_knowledge(self, item_id: int):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM knowledge_items WHERE id = ?", (item_id,))
        conn.commit()
        conn.close()
