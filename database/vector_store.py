import sqlite3
import json
import os
import requests
import math

DB_PATH = "database/elite_lance.db"
EMBEDDING_MODEL = "nomic-embed-text"

class OllamaEmbeddings:
    def __init__(self, model):
        self.model = model
    def __call__(self, input_texts):
        embeddings = []
        for text in input_texts:
            try:
                response = requests.post(
                    "http://localhost:11434/api/embeddings",
                    json={"model": self.model, "prompt": text},
                    timeout=120
                )
                embeddings.append(response.json()["embedding"])
            except Exception as e:
                print(f"Embedding error: {e}")
                embeddings.append([0.0] * 768) # Fallback for now
        return embeddings

def cosine_similarity(v1, v2):
    dot_product = sum(a * b for a, b in zip(v1, v2))
    magnitude1 = math.sqrt(sum(a * a for a in v1))
    magnitude2 = math.sqrt(sum(a * a for a in v2))
    if not magnitude1 or not magnitude2:
        return 0.0
    return dot_product / (magnitude1 * magnitude2)

class RankingEngine:
    def __init__(self):
        os.makedirs("database", exist_ok=True)
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()
        self._init_db()
        self.ollama_ef = OllamaEmbeddings(EMBEDDING_MODEL)

    def _init_db(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS portfolio (
                id TEXT PRIMARY KEY,
                content TEXT,
                embedding TEXT,
                metadata TEXT
            )
        ''')
        self.conn.commit()

    def add_documents(self, documents, metadatas, ids):
        embeddings = self.ollama_ef(documents)
        for doc, meta, id, emb in zip(documents, metadatas, ids, embeddings):
            self.cursor.execute(
                "INSERT OR REPLACE INTO portfolio (id, content, embedding, metadata) VALUES (?, ?, ?, ?)",
                (id, doc, json.dumps(emb), json.dumps(meta))
            )
        self.conn.commit()

    def search_and_rank(self, query_text, required_tech=None, top_k=2):
        query_embedding = self.ollama_ef([query_text])[0]
        
        self.cursor.execute("SELECT id, content, embedding, metadata FROM portfolio")
        rows = self.cursor.fetchall()
        
        results = []
        for row in rows:
            doc_id, content, emb_json, meta_json = row
            doc_embedding = json.loads(emb_json)
            metadata = json.loads(meta_json)
            
            # 1. Semantic Score (0.6)
            semantic_score = cosine_similarity(query_embedding, doc_embedding)
            
            # 2. Tech Match Score (0.2)
            tech_score = 0
            if required_tech:
                matches = set(required_tech) & set(metadata.get('tech_stack', []))
                tech_score = len(matches) / len(required_tech) if required_tech else 0
            
            # 3. Recency Score (0.1) - Mocked for now based on 'year' in metadata
            recency_score = 0.5 # Default
            
            # Final Hybrid Score
            final_score = (semantic_score * 0.6) + (tech_score * 0.2) + (recency_score * 0.2)
            
            results.append({
                "id": doc_id,
                "document": content,
                "metadata": metadata,
                "score": final_score
            })
            
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:top_k]

if __name__ == "__main__":
    engine = RankingEngine()
    print("Ranking Engine (Lite) Initialized.")
