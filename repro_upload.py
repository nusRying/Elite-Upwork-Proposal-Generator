import os
import sqlite3
import json
import shutil
import fitz  # pymupdf
from utils.knowledge_vault import KnowledgeVault

def create_test_pdf(path, text):
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((72, 72), text, fontname="helv", fontsize=12)
    doc.save(path)
    doc.close()

def test_ingestion():
    db_path = "test_data/portfolio.db"
    knowledge_dir = "test_data/knowledge"
    
    if os.path.exists("test_data"):
        shutil.rmtree("test_data")
    os.makedirs(knowledge_dir, exist_ok=True)
    
    kv = KnowledgeVault(db_path=db_path, knowledge_dir=knowledge_dir)
    
    test_pdf = os.path.join(knowledge_dir, "test.pdf")
    create_test_pdf(test_pdf, "This is a test PDF for Upwork Proposal Generator.")
    
    print(f"Ingesting {test_pdf}...")
    try:
        filename = kv.ingest_file(test_pdf)
        print(f"Successfully ingested {filename}")
        
        items = kv.get_all_knowledge()
        print(f"Found {len(items)} items in vault")
        for item in items:
            print(f"- {item['filename']}: {item['snippet']}...")
            
    except Exception as e:
        print(f"Ingestion failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_ingestion()
