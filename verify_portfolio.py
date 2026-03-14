from database.vector_store import RankingEngine

def verify_enrichment():
    engine = RankingEngine()
    
    test_queries = [
        "Shopify headless commerce",
        "RL drone vibration control",
        "Ollama and LangGraph AI"
    ]
    
    for query in test_queries:
        print(f"\nQuery: {query}")
        results = engine.search_and_rank(query, top_k=2)
        for i, res in enumerate(results):
            meta = res['metadata']
            print(f"{i+1}. Project: {meta.get('source', 'Unknown')}")
            print(f"   Link: {meta.get('link', 'N/A')}")
            print(f"   Skills: {', '.join(meta.get('tech_stack', []))}")
            print(f"   Score: {res['score']:.4f}")

if __name__ == "__main__":
    verify_enrichment()
