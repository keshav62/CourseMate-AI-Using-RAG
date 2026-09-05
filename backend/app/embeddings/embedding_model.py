from langchain_google_genai import GoogleGenerativeAIEmbeddings


def get_embedding_model():

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001"
    )

    return embeddings