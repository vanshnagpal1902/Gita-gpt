import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# -------------------------------
# Load API key
# -------------------------------

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

# -------------------------------
# Streamlit UI
# -------------------------------

st.set_page_config(page_title="GitaGPT", page_icon="🕉️")

st.title("🕉️ GitaGPT")
st.write("Ask life questions and receive wisdom from the Bhagavad Gita.")

# -------------------------------
# Load embeddings
# -------------------------------

@st.cache_resource
def load_vectorstore():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore

vectorstore = load_vectorstore()

retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

# -------------------------------
# Chat input
# -------------------------------

user_question = st.text_input("Ask your question")

if user_question:

    docs = retriever.invoke(user_question)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a wise spiritual guide explaining teachings from the Bhagavad Gita.

User Problem:
{user_question}

Relevant verses:
{context}

Respond using this format:

भगवद्गीता अध्याय <chapter>, श्लोक <verse>

संस्कृत श्लोक:
<verse>

रोमन ट्रांसलिटरेशन:

हिन्दी अनुवाद:

English Translation:

Explanation:
Explain calmly how the verse applies to the user's life problem.
"""

    with st.spinner("Consulting the wisdom of the Gita..."):

        chat = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6
        )

        answer = chat.choices[0].message.content

    st.markdown("### 🕉️ GitaGPT says:")
    st.write(answer)