from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


def create_vector_store(chunks):

    print(f"Creating embeddings for {len(chunks)} chunks...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )

    print("Vector store created successfully.")

    return vector_store