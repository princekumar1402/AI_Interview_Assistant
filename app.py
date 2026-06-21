import streamlit as st
import os
from src.resume_parser import load_and_split_resume
from src.resume_analyzer import (
    analyze_resume,
    review_resume,
    extract_resume_score
)
from src.vector_store import create_vector_store, get_retriever
from src.report_generator import generate_report
from src.interview_engine import (
    start_interview,
    process_answer
)
st.set_page_config(
    page_title="AI Interview Assistant",
    page_icon="🤖"
)

st.title("🤖 AI Interview Assistant")

# Role Selection
role = st.selectbox(
    "Select Interview Role",
    [
        "AI/ML Engineer",
        "Data Scientist",
        "Software Engineer",
        "Full Stack Developer",
        "Backend Developer"
    ]
)

difficulty = st.selectbox(
    "Select Difficulty",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

# Session State

if "interview_evaluated" not in st.session_state:
    st.session_state.interview_evaluated = False

if "questions" not in st.session_state:
    st.session_state.questions = []

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "feedback" not in st.session_state:
    st.session_state.feedback = ""

if "interview_started" not in st.session_state:
    st.session_state.interview_started = False

if "resume_analysis" not in st.session_state:
    st.session_state.resume_analysis = ""

if "resume_review" not in st.session_state:
    st.session_state.resume_review = ""

if "resume_analyzed" not in st.session_state:
    st.session_state.resume_analyzed = False
if "answers" not in st.session_state:
    st.session_state.answers = []

if "interview_evaluated" not in st.session_state:
    st.session_state.interview_evaluated = False
if "final_report" not in st.session_state:
    st.session_state.final_report = ""


# Resume Upload

uploaded_file = st.file_uploader(
    "Upload Your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    save_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Resume Uploaded Successfully!")

  
# Analyze Resume

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            chunks = load_and_split_resume(
                save_path
            )

            analysis = analyze_resume(
                chunks
            )

            review = review_resume(
                chunks
            )

            st.session_state.resume_analysis = analysis
            st.session_state.resume_review = review
            st.session_state.resume_analyzed = True

        st.rerun()

# Show Resume Analysis

if st.session_state.resume_analyzed:

    st.subheader("📄 Resume Summary")

    st.write(
        st.session_state.resume_analysis
    )
    resume_score = extract_resume_score(
        st.session_state.resume_review
    )
    if resume_score is not None:
        st.subheader("📈 Resume Score")
        st.write(f"Your resume score is: {resume_score}")

    st.subheader("📊 Resume Review")

    st.write(
        st.session_state.resume_review
    )

# Start Interview

    if st.button("Start Interview"):

        with st.spinner(
            "Generating Interview Questions..."
        ):

            chunks = load_and_split_resume(
                save_path
            )

            vector_store = create_vector_store(
                chunks
            )

            retriever = get_retriever(
                vector_store
            )

            questions = start_interview(
                retriever,
                role,
                difficulty
            )

        st.session_state.questions = questions
        st.session_state.current_question = 0
        st.session_state.interview_started = True
        st.session_state.feedback = ""

        st.rerun()

# Interview Section

if st.session_state.interview_started:

    current_idx = st.session_state.current_question

    # Show Previous Questions & Answers

    if st.session_state.answers:

        st.subheader("📜 Interview History")

        for item in st.session_state.answers:

            st.markdown(
                f"🤖 **Question:** {item['question']}"
            )

            st.markdown(
                f"👤 **Answer:** {item['answer']}"
            )

            st.divider()

 # Show Evaluation Button After 3 Answers

    if len(st.session_state.answers) >= 3:

        st.success(
            f"{len(st.session_state.answers)} questions answered"
        )

        if st.button("Evaluate Interview"):

            st.session_state.interview_evaluated = True

            st.rerun()
        if st.session_state.interview_evaluated:

            if not st.session_state.final_report:

              with st.spinner(
            "Generating Interview Report..."
        ):

               report = generate_report(
                st.session_state.answers
            )

            st.session_state.final_report = report

            st.header(
                 "📊 Interview Report"
                )

    st.write(
        st.session_state.final_report
    )

# Show Current Question

    if current_idx < len(st.session_state.questions):

        question = st.session_state.questions[current_idx]

        st.subheader(
            f"Question {current_idx + 1}"
        )

        st.write(question)

        answer = st.text_area(
            "Your Answer",
            height=200,
            key=f"answer_{current_idx}"
        )

        if st.button("Save Answer"):

            if answer.strip():

                st.session_state.answers.append(
                    {
                        "question": question,
                        "answer": answer
                    }
                )

                st.session_state.current_question += 1

                st.rerun()

            else:

                st.warning(
                    "Please enter an answer."
                )

    else:

        st.success(
            "🎉 All Questions Completed!"
        )

        if st.button("Evaluate Interview"):

            st.session_state.interview_evaluated = True

            st.rerun()