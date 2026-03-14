name:	nusRying/multilingual-text-intelligence
description:	
--
# ≡ƒîì Multilingual Text Intelligence System

A high-performance NLP pipeline designed for **English** and **Arabic** text processing. This system provides a unified interface for data cleaning, sentiment analysis, topic modeling, and semantic search, leveraging state-of-the-art transformer models.

---

## ≡ƒÜÇ Advanced Features

- **Granular NLP**: Named Entity Recognition (NER) and 7-category Emotion Detection.
- **Arabic Optimization**: AraBERT integration for high-precision Arabic sentiment analysis.
- **Production Scaling**: Pinecone vector database support and ONNX Runtime inference optimization.
- **Interactive Analytics**: 2D Topic Mapping (UMAP) and automated trend alerts.
- **Live Data**: Reddit live ingestion connector.
- **Docker Ready**: Full containerized deployment with `docker-compose`.

---

## ≡ƒÅù System Architecture

The system follows a modular pipeline:

1.  **Ingestion**: Fetch data from various sources (Mock APIs, CSVs, Reddit).
2.  **Preprocessing**: Clean and normalize text, detect language.
3.  **Embeddings**: Generate dense vectors using HuggingFace Transformers.
4.  **Task Models**: Sentiment (ML/AR), Emotions, NER, and Topics.
5.  **Interface**: Dashboard (Streamlit) and API (FastAPI).

---

## ≡ƒ¢á Tech Stack

- **Language**: Python 3.9+
- **NLP Frameworks**: `transformers`, `sentence-transformers`, `torch`, `praw`
- **Web Framework**: `FastAPI`
- **Visualization**: `Streamlit`, `Plotly`, `umap-learn`
- **Data Handling**: `pandas`, `numpy`, `fpdf2`
- **Inference**: `onnxruntime`
- **Vector Search**: Pinecone / Local FAISS

---

## ≡ƒÜª Getting Started

### 1. Installation

Clone the repository:

```bash
git clone https://github.com/nusRying/multilingual-text-intelligence.git
cd multilingual-text-intelligence
```

### 2. Run with Docker (Recommended)

```bash
docker-compose up --build
```

This starts the API (8000) and Dashboard (8501) automatically.

### 3. Manual Setup

Create and activate a virtual environment:

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run services:

```bash
python main.py             # API at http://127.0.0.1:8000
streamlit run dashboard.py  # Dashboard at http://localhost:8501
```

### 4. Performance Optimization

To convert models to ONNX for faster inference:

```bash
python scripts/optimize_onnx.py --model aubmindlab/bert-base-arabertv02 --output ./onnx_models/arabert
```

---

## ≡ƒôé Project Structure

```text
Γö£ΓöÇΓöÇ src/
Γöé   Γö£ΓöÇΓöÇ ingestion/     # Data connectors (Mock APIs, CSV, Reddit)
Γöé   Γö£ΓöÇΓöÇ models/        # Sentiment, Emotions, NER, Topics, Search
Γöé   Γö£ΓöÇΓöÇ preprocessing/ # English and Arabic text cleaners
Γöé   ΓööΓöÇΓöÇ utils/         # Vector store (Local/Pinecone) and helpers
Γö£ΓöÇΓöÇ scripts/           # Optimization scripts (ONNX)
Γö£ΓöÇΓöÇ tests/             # Pytest suite
Γö£ΓöÇΓöÇ dashboard.py       # Streamlit application
Γö£ΓöÇΓöÇ main.py            # FastAPI service
Γö£ΓöÇΓöÇ Dockerfile         # Container definition
Γö£ΓöÇΓöÇ docker-compose.yml # Service orchestration
ΓööΓöÇΓöÇ requirements.txt   # Project dependencies
```

---

## ≡ƒº¬ Testing

Run the test suite:

```bash
python -m pytest
```

---

## ≡ƒôä License

This project is licensed under the MIT License.

