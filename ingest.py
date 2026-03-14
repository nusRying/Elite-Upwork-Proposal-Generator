import os
import re
import fitz  # PyMuPDF
from database.vector_store import RankingEngine

# Configuration
PORTFOLIO_DIR = "portfolio"

def simple_text_splitter(text, chunk_size=1000, chunk_overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - chunk_overlap
    return chunks

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def ingest_portfolio():
    if not os.path.exists(PORTFOLIO_DIR):
        os.makedirs(PORTFOLIO_DIR)
        print(f"Created {PORTFOLIO_DIR} folder. Please add your projects there.")
        return

    engine = RankingEngine()
    
    files = [f for f in os.listdir(PORTFOLIO_DIR) if f.endswith(('.pdf', '.txt', '.md'))]
    
    for filename in files:
        file_path = os.path.join(PORTFOLIO_DIR, filename)
        print(f"Processing {filename}...")
        
        if filename.endswith('.pdf'):
            content = extract_text_from_pdf(file_path)
        else:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
        chunks = simple_text_splitter(content)
        
        # Parse fields from the structured text
        repo_link = ""
        skills = []
        link_match = re.search(r'Link: (https?://[^\n]+)', content)
        if link_match:
            repo_link = link_match.group(1)
            
        skills_match = re.search(r'Skills: ([^\n]+)', content)
        if skills_match:
            skills = [s.strip() for s in skills_match.group(1).split(',')]

        metadata = {
            "source": filename,
            "link": repo_link,
            "tech_stack": skills
        }
        
        ids = [f"{filename}_{i}" for i in range(len(chunks))]
        metadatas = [metadata for _ in range(len(chunks))]
        
        engine.add_documents(chunks, metadatas, ids)
            
    print(f"Successfully ingested {len(files)} files.")

if __name__ == "__main__":
    ingest_portfolio()
