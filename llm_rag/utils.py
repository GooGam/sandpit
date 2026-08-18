import numpy as np
import ollama

def get_embedding(text):
    """Generate embedding using Ollama."""
    # response is a JSON object (parsed as a dictionary) with an "embedding" key
    # containing a list of floating-point numbers
    response = ollama.embeddings(model="embeddinggemma", prompt=text)
    # np.array returns a n-dimentional numpy array
    return np.array(response["embedding"])

def chunk_text(text, chunk_size=500):
    """Simple character-based chunking."""
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def search_index(query_embedding, index, chunks, top_k=2):
    """Find top_k chunks based on cosine similarity."""
    # dot product of query embedding and each chunk embedding
    # since embeddings are normalized, the dot product is equivalent to cosine similarity
    similarities = [np.dot(query_embedding, chunk_emb) for chunk_emb in index]
    # argsort returns the indices that would sort the array.
    # by default, it sorts in ascending order 
    # (larger cosine similarity means more similar, so we want the last top_k indices).
    # so we take the last top_k indices and reverse them for descending order.
    top_indices = np.argsort(similarities)[-top_k:][::-1]
    return [chunks[i] for i in top_indices]

def generate_answer(query, context):
    """Generate grounded answer using Gemma 3."""
    prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"
    response = ollama.chat(model="gemma3:1b", messages=[{'role': 'user', 'content': prompt}])
    # The ollama library returns a complex JSON structure.
    # Extract just the text of the actual answer, stripping away technical metadata 
    # (like the model name, timing, or token usage statistics).
    return response['message']['content']
