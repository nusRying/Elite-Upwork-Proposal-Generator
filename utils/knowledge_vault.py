import os
from typing import List
from pypdf import PdfReader
from docx import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
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
            reader = PdfReader(file_path)
            for page in reader.pages:
                content += page.extract_text() + "\n"
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
        cursor.execute("SELECT id, filename, content FROM knowledge_items")
        items = [{"id": r[0], "filename": r[1], "snippet": r[2][:200]} for r in cursor.fetchall()]
        conn.close()
        return items

    def delete_knowledge(self, item_id: int):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM knowledge_items WHERE id = ?", (item_id,))
        conn.commit()
        conn.close()
