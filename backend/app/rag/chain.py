from langchain_google_genai import ChatGoogleGenerativeAI


def get_llm():

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        temperature=0
    )

    return llm


def build_prompt(context, question):

    prompt = f"""
              You are CourseMate AI, an AI study assistant.

              Answer the student's question using ONLY the
              provided study material.

              Rules:
              1. Use the provided context.
              2. Do not invent information.
              3. If the answer cannot be found in the context,
                clearly say that the information was not found
                in the uploaded study material.
              4. Explain the answer clearly for a student.
              5. Give the relevant source/page information when available.

              Study Material:
              {context}

              Student Question:
              {question}

              Answer:
              """

    return prompt

def ask_question(retriever, question):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    llm = get_llm()

    prompt = build_prompt(
        context,
        question
    )

    response = llm.invoke(prompt)

    return response.content, docs