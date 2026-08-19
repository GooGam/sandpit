import numpy as np
import ollama
import pandas as pd

def read_xls_to_text(file_path):
    """Read .xls file and convert content to a single string."""
    df = pd.read_excel(file_path)
    # Convert dataframe to string representation
    return df.to_string()

def read_txt_to_text(file_path):
    """Read .txt file and convert content to a single string."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

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

def read_xls_to_chunks(file_path):
    """Read .xls file and return list of chunked strings with headers (one row per chunk)."""
    chunks = []
    df = pd.read_excel(file_path)

    for i in range(0, len(df)):
        chunk_df = df.iloc[i:i+1]  # Get single row
        chunk_content = chunk_df.to_string(index=False)
        chunks.append(chunk_content)
    return chunks

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
    # print(f"DEBUG: context: {context} ")
    prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"
    response = ollama.chat(model="llama3.2:latest", messages=[{'role': 'user', 'content': prompt}])
    # The ollama library returns a complex JSON structure.
    # Extract just the text of the actual answer, stripping away technical metadata 
    # (like the model name, timing, or token usage statistics).
    return response['message']['content']
