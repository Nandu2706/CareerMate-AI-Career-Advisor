
from agent import generate_career_advice

question = """
I am a first-year BTech student.
I know basic Python.
I want to become a software engineer.
Create a learning roadmap for me.
"""

answer = generate_career_advice(
    question,
    session_id="student_001"
)

print("\n===== CAREERMATE RESPONSE =====\n")
print(answer)
