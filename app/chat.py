import os
from dotenv import load_dotenv
from groq import Groq

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# ---------------------------------------------------
# Load environment variables
# ---------------------------------------------------

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

client = Groq(api_key=api_key)

# ---------------------------------------------------
# Load embedding model
# ---------------------------------------------------

print("Loading embedding model...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ---------------------------------------------------
# Load FAISS vector database
# ---------------------------------------------------

print("Loading Bhagavad Gita knowledge base...")

vectorstore = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}
)

print("\n🕉️ GitaGPT is ready.")
print("Ask your life question or type 'exit' to quit.\n")

# ---------------------------------------------------
# Chat loop
# ---------------------------------------------------

while True:

    user = input("You: ")

    if user.lower() == "exit":
        print("🙏 Goodbye. May you find clarity and peace.")
        break

    # -----------------------------------------------
    # Retrieve relevant verses
    # -----------------------------------------------

    docs = retriever.invoke(user)

    context = "\n\n".join([doc.page_content for doc in docs])

    # -----------------------------------------------
    # Build prompt
    # -----------------------------------------------

    prompt = f"""
You are a wise spiritual guide explaining teachings from the Bhagavad Gita.

A person has come with a life problem.

User Problem:
{user}

Relevant Bhagavad Gita verses:
{context}

Respond using this structured format:

भगवद्गीता अध्याय <chapter>, श्लोक <verse>

संस्कृत श्लोक:
<show the Sanskrit verse>

रोमन ट्रांसलिटरेशन:
<show transliteration if available>

हिन्दी अनुवाद (सरल अर्थ):
<give a simple Hindi meaning>

English Translation:
<give a clear English translation>

Explanation:
Explain calmly how this teaching from the Bhagavad Gita applies to the user's problem.
Give thoughtful spiritual guidance.

If multiple verses are relevant, choose the most appropriate one.
"""

    # -----------------------------------------------
    # Call Groq LLM
    # -----------------------------------------------

    chat = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6
    )

    ai_reply = chat.choices[0].message.content

    print("\n🕉️ GitaGPT:\n")
    print(ai_reply)
    print("\n")