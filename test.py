from src.resume_parser import load_and_split_resume
from src.resume_analyzer import analyze_resume

chunks = load_and_split_resume(
    "uploads/resume.pdf"
)

analysis = analyze_resume(chunks)

print(analysis)