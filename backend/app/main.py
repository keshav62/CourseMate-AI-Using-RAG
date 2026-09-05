from dotenv import load_dotenv

from app.loaders.pdf_loader import load_pdf
from app.utils.text_utils import split_documents
from app.vectorstore.chroma import create_vector_store
from app.rag.retriever import get_retriever
from app.rag.chain import ask_question


load_dotenv()


PDF_PATH = "data/documents/Rich-Dad-Poor-Dad-2.pdf"


def main():

    print("Loading PDF...")

    documents = load_pdf(PDF_PATH)

    print(f"Loaded {len(documents)} pages.")

    print("Creating chunks...")

    chunks = split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    print("Creating vector database...")

    vector_store = create_vector_store(chunks)

    print("Vector database ready.")

    retriever = get_retriever(vector_store)

    print("\nCourseMate AI is ready!")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("You: ")

        if question.lower() == "exit":
            break

        answer, sources = ask_question(
            retriever,
            question
        )

        print("\nCourseMate:")
        print(answer)

        print("\nSources:")

        for doc in sources:

            page = doc.metadata.get("page")

            print(
                f"- Page {page + 1 if page is not None else 'Unknown'}"
            )

        print()


if __name__ == "__main__":
    main()