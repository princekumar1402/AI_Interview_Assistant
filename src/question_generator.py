from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from src.config import MODEL_NAME
load_dotenv()
from src.prompts import QUESTION_GENERATION_PROMPT
def generate_questions(
    retriever,
    role,
    difficulty
):

    docs = retriever.invoke(
        "Give complete information about skills, projects, education and technologies."
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    llm = ChatGroq(
        model=MODEL_NAME,
        temperature=0.7
    )

    prompt = ChatPromptTemplate.from_template(
        QUESTION_GENERATION_PROMPT
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "context": context,
            "role": role,
            "difficulty": difficulty
        }
    )

    questions = []

    for line in response.content.split("\n"):

        line = line.strip()

        if line and line[0].isdigit():
            questions.append(line)

    return questions