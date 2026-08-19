import numpy as np
import pandas as pd
from utils import read_txt_to_text, read_pdf_to_text, get_embedding, chunk_text, search_index, generate_answer

# 1. Source Data
# text = read_txt_to_text("data/cano.txt")
text = read_pdf_to_text("data/scan.pdf")
# df_text = pd.read_excel("data/median-house-q4-2025.xls")

# 2. Chunking
chunks = chunk_text(text)
# chunks = read_xls_to_chunks("data/median-house-q4-2025.xls")

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
