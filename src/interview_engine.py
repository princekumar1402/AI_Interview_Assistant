from src.question_generator import generate_questions
from src.evaluator import evaluate_answer


def start_interview(
    retriever,
    role,
    difficulty
):
    return generate_questions(
        retriever,
        role,
        difficulty
    )

def process_answer(question, answer):

    feedback = evaluate_answer(
        question=question,
        answer=answer
    )

    return feedback