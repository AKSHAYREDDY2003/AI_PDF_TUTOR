from sentence_transformers import CrossEncoder

# Load reranker model
reranker_model = CrossEncoder("BAAI/bge-reranker-large")

def rerank_docs(question, docs, top_k=3):
    # Create (query, document) pairs
    pairs = [(question, doc.page_content) for doc in docs]

    # Get relevance scores
    scores = reranker_model.predict(pairs)

    # Combine scores with docs and sort
    ranked_docs = [
        doc for _, doc in sorted(
            zip(scores, docs),
            key=lambda x: x[0],
            reverse=True
        )
    ]

    # Return top documents
    return ranked_docs[:top_k]