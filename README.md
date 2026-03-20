
# 🕉️ GitaGPT – AI-Powered Bhagavad Gita Assistant

GitaGPT is an intelligent **AI-powered chatbot** that provides life guidance using the teachings of the **Bhagavad Gita**. It uses a **Retrieval-Augmented Generation (RAG)** pipeline to fetch relevant verses and generate meaningful, contextual explanations.

---

## 🚀 Features

* 📖 Ask life questions and receive answers based on Bhagavad Gita teachings
* 🔍 Semantic search using **vector embeddings (FAISS)**
* 🧠 Context-aware responses using **LLMs (Groq / Ollama)**
* 🕉️ Structured output:

  * Sanskrit Shloka
  * Transliteration
  * Hindi Translation
  * English Translation
  * Practical Explanation
* 🌐 Browser-based UI using **Streamlit**

---

## 🧠 How It Works (Architecture)

```id="z3o4nq"
Bhagavad Gita PDF
        ↓
Text Extraction
        ↓
Chunking (semantic)
        ↓
Embeddings (Sentence Transformers)
        ↓
FAISS Vector Database
        ↓
User Query
        ↓
Similarity Search (Top-K)
        ↓
LLM (Groq / Ollama)
        ↓
Structured Response
```

---

## 🛠️ Tech Stack

* **Language:** Python
* **Vector DB:** FAISS
* **Embeddings:** Sentence-Transformers (`all-MiniLM-L6-v2`)
* **LLMs:**

  * Groq API (`llama-3.1-8b-instant`)
  * Ollama (local models)
* **Frameworks:** LangChain
* **Frontend:** Streamlit

---

## 📂 Project Structure

```id="k6tqxt"
gita-gpt/
│
├── data/
│   └── gita.pdf
│
├── scripts/
│   └── ingest.py        # Creates vector database
│
├── vectorstore/         # FAISS index (generated)
│
├── app/
│   ├── chat.py          # CLI chatbot
│   └── webapp.py        # Streamlit UI
│
├── .env                 # API keys
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash id="q4q1ox"
git clone https://github.com/yourusername/gita-gpt.git
cd gita-gpt
```

---

### 2. Create virtual environment

```bash id="m9rr3g"
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash id="qzj4is"
pip install -r requirements.txt
```

---

### 4. Add API Key

Create a `.env` file:

```id="1t8bmn"
GROQ_API_KEY=your_api_key_here
```

---

### 5. Run ingestion (one-time)

```bash id="i6s2f6"
python scripts/ingest.py
```

This creates:

```id="4epj7r"
vectorstore/
   index.faiss
   index.pkl
```

---

### 6. Run the chatbot

#### CLI Version

```bash id="cs5x6c"
python app/chat.py
```

#### Web App (Recommended)

```bash id="8z8vls"
streamlit run app/webapp.py
```

Then open:

```id="oz36yr"
http://localhost:8501
```

---

## 💡 Example Query

```id="5fuhq1"
User: I feel anxious about my future
```

**Response:**

* Bhagavad Gita Chapter 2 Verse 47
* Sanskrit verse
* Hindi & English translation
* Practical explanation about detachment and focus on action

---

## 🌟 Key Learnings

* Built a complete **RAG pipeline from scratch**
* Learned how **vector databases enable semantic search**
* Integrated both **local (Ollama)** and **cloud LLMs (Groq)**
* Understood real-world **GenAI system design**

---

## 🚧 Future Improvements

* Verse-level structured dataset (chapter + verse metadata)
* Reranking for better retrieval accuracy
* Emotion-aware responses (fear, anger, confusion)
* Multi-language support
* Deployment (Render / AWS / Vercel)

---

## 🤝 Contributing

Feel free to fork the repo and improve the system. Suggestions and pull requests are welcome!

---

## 📜 License

This project is for educational purposes and inspired by the teachings of the Bhagavad Gita.

---

## 🙏 Acknowledgement

Inspired by the timeless wisdom of the **Bhagavad Gita** and the power of modern **Generative AI systems**.

---


