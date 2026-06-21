from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config import MODEL_NAME
from src.prompts import EVALUATION_PROMPT
load_dotenv()


def evaluate_answer(question, answer):

    llm = ChatGroq(
        model=MODEL_NAME,
        temperature=0
    )

    prompt = ChatPromptTemplate.from_template(
        EVALUATION_PROMPT
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "question": question,
            "answer": answer
        }
    )

    return response.content