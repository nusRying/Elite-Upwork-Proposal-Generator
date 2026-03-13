import os
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
    
    files = [f for f in os.listdir(PORTFOLIO_DIR) if f.endswith(('.pdf', '.txt'))]
    
    for filename in files:
        file_path = os.path.join(PORTFOLIO_DIR, filename)
        print(f"Processing {filename}...")
        
        if filename.endswith('.pdf'):
            content = extract_text_from_pdf(file_path)
        else:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
        chunks = simple_text_splitter(content)
        
        metadata = {
            "source": filename,
            "tech_stack": []
        }
        
        keywords = ["SolidWorks", "Python", "Shopify", "React", "AI", "nTopology"]
        for kw in keywords:
            if kw.lower() in content.lower():
                metadata["tech_stack"].append(kw)
        
        ids = [f"{filename}_{i}" for i in range(len(chunks))]
        metadatas = [metadata for _ in range(len(chunks))]
        
        engine.add_documents(chunks, metadatas, ids)
            
    print(f"Successfully ingested {len(files)} files.")

if __name__ == "__main__":
    ingest_portfolio()
