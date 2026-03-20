from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

print("Loading Bhagavad Gita PDF...")

loader = PyPDFLoader("data/gita.pdf")
documents = loader.load()

print(f"Loaded pages: {len(documents)}")

# Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)

print(f"Total chunks created: {len(chunks)}")

# Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Embedding model loaded")

# Create vector database
vectorstore = FAISS.from_documents(chunks, embeddings)

# Save it permanently
vectorstore.save_local("vectorstore")

print("Vector database created and saved successfully")