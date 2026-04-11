from openai import OpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="Learning_RAG",
    embedding=embeddings,
)

def process_query(query: str):
    print("🔍 Searching Chunks:", query)

    search_result = vector_db.similarity_search(query=query, k=3)

    if not search_result:
        return "No relevant context found."

    context = "\n\n".join([
        f"[Page {r.metadata.get('page', 'N/A')}]\n{r.page_content}"
        for r in search_result
    ])

    SYSTEM_PROMPT = f"""
You are a precise assistant.
Answer only from the provided context.
If missing info, say you don't know.
Keep it concise (max 3-5 sentences).
Mention page numbers if possible.

Context:
{context}
"""

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": query}
        ]
    )

    answer = response.choices[0].message.content
    print("💬 Response:", answer)

    return answer