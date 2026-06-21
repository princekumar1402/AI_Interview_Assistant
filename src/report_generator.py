from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from src.config import MODEL_NAME

load_dotenv()


def generate_report(interview_answers):

    interview_text = ""

    for item in interview_answers:

        interview_text += f"""
Question:
{item['question']}

Answer:
{item['answer']}

--------------------------------
"""

    llm = ChatGroq(
        model=MODEL_NAME,
        temperature=0
    )

    prompt = ChatPromptTemplate.from_template(
        """
You are a senior technical interviewer.

Evaluate the complete interview.

Interview Data:

{interview_data}

Generate:

1. Overall Score (out of 10)
2. Technical Knowledge Score
3. Communication Score
4. Project Understanding Score

5. Strengths
6. Weaknesses
7. Improvement Areas
8. Recommended Topics to Study

Return a professional interview report.
"""
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "interview_data": interview_text
        }
    )

    return response.content