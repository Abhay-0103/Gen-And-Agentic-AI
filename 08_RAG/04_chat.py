from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
api_key = os.getenv("GEMINI_API_KEY"),
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

# Taking user input
user_query = input("Kuch Tho Puch le BSDK: ")

# Relevant chunks from the vectorDB for the user query
search_result = vector_db.similarity_search(query=user_query, k=3)

context = "\n\n".join([
    f"[Page {result.metadata.get('page', 'N/A')}]\n{result.page_content}"
    for result in search_result
])

SYSTEM_PROMPT = f"""
You are a precise assistant.

Answer only from the provided context.
If missing info, say you don't know.

Keep it concise (max 3-5 sentences).

If possible, mention the page number(s) from the context where the answer was found.
If the user wants more details, suggest checking those page numbers.
Context:
{context}
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {user_query}"
        }
    ]
)

print(f"Response: {response.choices[0].message.content}")