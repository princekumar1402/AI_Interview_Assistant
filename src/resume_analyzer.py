from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from src.config import MODEL_NAME

load_dotenv()

def review_resume(chunks):

    resume_text = "\n\n".join(
        [chunk.page_content for chunk in chunks]
    )

    llm = ChatGroq(
        model=MODEL_NAME,
        temperature=0
    )

    prompt = ChatPromptTemplate.from_template(
        """
You are an expert technical recruiter.

Analyze the resume and provide:

1. Resume Score (out of 100)
2. Overall Assessment
3. Strengths
4. Weaknesses
5. Missing Skills
6. Suggestions for Improvement

Resume:

{resume}

Return in this format:

Resume Score: XX/100

Overall Assessment:
...

Strengths:
- ...

Weaknesses:
- ...

Missing Skills:
- ...

Suggestions:
- ...
"""
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "resume": resume_text
        }
    )

    return response.content

def analyze_resume(chunks):

    resume_text = "\n\n".join(
        [chunk.page_content for chunk in chunks]
    )

    llm = ChatGroq(
        model=MODEL_NAME,
        temperature=0
    )

    prompt = ChatPromptTemplate.from_template(
        """
You are an expert resume analyzer.

Analyze the resume and provide:

1. Professional Summary
2. Skills
3. Projects
4. Education
5. Experience
6. Certifications (if any)

Resume:

{resume}

Return the result in a clean structured format.
"""
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "resume": resume_text
        }
    )

    return response.content

import re
def extract_resume_score(review_text):

    match = re.search(
        r"Resume Score:\s*(\d+)",
        review_text
    )

    if match:
        return int(match.group(1))

    return None