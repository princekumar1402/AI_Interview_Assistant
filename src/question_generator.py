from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from src.config import MODEL_NAME

load_dotenv()


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
        """
You are a senior technical interviewer.

Candidate Resume:
{context}

Target Role:
{role}

Difficulty:
{difficulty}

Generate exactly 10 interview questions.

Question Distribution:

- 3 questions about candidate projects
- 3 questions about role-specific concepts
- 2 questions about core fundamentals
- 2 scenario/problem-solving questions

Rules:

- Match the selected role strongly.
- Match the selected difficulty.
- Do not generate all questions from a single project.
- Cover different skills from the resume.
- Simulate a real technical interview.

Return only numbered questions.

"""
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