import numpy as np
from utils import get_embedding, chunk_text, search_index, generate_answer

# 1. Source Data
text = "The quick brown fox jumps over the lazy dog. Local RAG pipelines are efficient for data privacy. Gemma 3 is a powerful model for local inference."

# 2. Chunking
chunks = chunk_text(text)

# 3. Indexing
index = [get_embedding(chunk) for chunk in chunks]
index = np.array(index)

def run_rag_pipeline(query):
    query_embedding = get_embedding(query)
    context = search_index(query_embedding, index, chunks)
    # a single coherent text blob to process, 
    # and the list of chunks needs to be flattened into that format.
    # " " is the separator to join the chunks
    answer = generate_answer(query, " ".join(context))
    return answer

# 4. Interactive Loop
if __name__ == "__main__":
    print("RAG Pipeline is ready! Type 'exit' to quit.")
    while True:
        try:
            query = input("\nQuery: ")
        except EOFError:
            break
        if query.lower() == 'exit':
            break
        answer = run_rag_pipeline(query)
        print(f"Answer: {answer}")
