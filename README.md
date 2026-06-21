# 🤖 AI Interview Assistant

An AI-powered Interview Preparation Platform that analyzes resumes, generates personalized interview questions, evaluates candidate answers, and provides detailed interview performance reports.

Built using **Streamlit, LangChain, Groq, Hugging Face Embeddings, and FAISS**.

---

## 🚀 Live Demo

Demo Link: ___________________________

---

## 📂 GitHub Repository

Repository Link: ___________________________

---

## 📌 Project Overview

AI Interview Assistant helps students and job seekers prepare for technical interviews by:

* Analyzing uploaded resumes
* Generating personalized interview questions
* Conducting mock interviews
* Evaluating candidate responses
* Generating interview performance reports
* Providing actionable improvement suggestions

The application simulates a realistic interview experience tailored to the candidate's resume and selected role.

---

## ✨ Features

### 📄 Resume Analysis

* Upload PDF resumes
* Extract resume content using PyPDFLoader
* Analyze:

  * Skills
  * Projects
  * Education
  * Experience
  * Certifications
* Generate resume summary
* Generate resume review and score

### 🎯 Role-Based Interviews

Supported roles:

* AI/ML Engineer
* Data Scientist
* Software Engineer
* Full Stack Developer
* Backend Developer

Questions are customized according to the selected role.

### 📈 Difficulty Levels

* Beginner
* Intermediate
* Advanced

Question complexity changes based on the selected level.

### 🧠 RAG-Based Question Generation

* Resume chunking using RecursiveCharacterTextSplitter
* Embedding generation using Hugging Face Embeddings
* FAISS Vector Database
* Semantic Retrieval
* Personalized question generation using resume context

### 💬 Mock Interview System

* One question at a time
* Interview history tracking
* Chat-like interview flow
* Resume-aware questioning

### 📝 Answer Evaluation

Evaluates answers based on:

* Technical Accuracy
* Clarity
* Depth of Knowledge
* Communication Skills
* Problem Solving Ability

Provides:

* Overall Score
* Strengths
* Weaknesses
* Improved Answer Suggestions

### 📊 Interview Report

Generates a detailed report containing:

* Overall Interview Score
* Technical Knowledge Assessment
* Communication Assessment
* Project Understanding Assessment
* Strengths
* Weaknesses
* Improvement Areas
* Recommended Topics to Study

---

## 🏗️ Architecture

```text
Resume Upload
      │
      ▼
PDF Parsing
(PyPDFLoader)
      │
      ▼
Text Chunking
(RecursiveCharacterTextSplitter)
      │
      ▼
Embeddings
(HuggingFace Embeddings)
      │
      ▼
FAISS Vector Store
      │
      ▼
Retriever
      │
      ▼
Question Generation
(Groq LLM)
      │
      ▼
Mock Interview
      │
      ▼
Answer Evaluation
      │
      ▼
Final Interview Report
```

## 🛠️ Tech Stack

### Frontend

* Streamlit

### LLM

* Groq
* Llama 3

### Framework

* LangChain

### Vector Database

* FAISS

### Embeddings

* Hugging Face Embeddings
* all-MiniLM-L6-v2

### Document Processing

* PyPDFLoader

### Environment Management

* Python Dotenv

---

## 📁 Project Structure

```text
AI_Interview_Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── uploads/
│
├── src/
│   ├── config.py
│   ├── prompts.py
│   ├── resume_parser.py
│   ├── resume_analyzer.py
│   ├── vector_store.py
│   ├── question_generator.py
│   ├── evaluator.py
│   ├── interview_engine.py
│   └── report_generator.py
```

## ⚙️ Installation

### Clone Repository

```bash
git clone YOUR_REPOSITORY_LINK
cd AI_Interview_Assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

### Run Application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

### Resume Upload

Screenshot: ___________________________

### Resume Analysis

Screenshot: ___________________________

### Interview Interface

Screenshot: ___________________________

### Interview Report

Screenshot: ___________________________

---

## 🎯 Future Improvements

* Follow-up Questions
* Voice-Based Interviews
* PDF Report Download
* Resume Role Match Score
* Study Plan Generation
* Interview Analytics Dashboard
* Multi-Round Interviews

