
from config import gemini_client, MODEL_NAME
from search import search_career_information
from memory import save_message, format_history


SYSTEM_PROMPT = """
You are CareerMate, an intelligent and friendly AI Career Advisor.

Your main goal is to help college students and fresh graduates
make informed career decisions.

YOUR RESPONSIBILITIES:
1. Recommend suitable career paths.
2. Identify in-demand technical skills.
3. Explain job roles and responsibilities.
4. Provide salary information.
5. Create personalized learning roadmaps.
6. Recommend courses and certifications.
7. Help students prepare for interviews and resumes.

YOUR PERSONALITY:
- Be friendly and supportive.
- Explain everything in simple English.
- Use headings and bullet points.
- Give practical examples.
- Ask follow-up questions when necessary.

ACCURACY RULES:
- Use web search for current career information.
- Never invent job openings or salary statistics.
- Clearly identify salary estimates and predictions.
- Include source URLs when available.
- Consider India as the default job market.
- Never guarantee employment or salary.

RESPONSE FORMAT:
1. Recommended Career
2. Why It Matches the Student
3. Required Skills
4. Expected Salary Range
5. Learning Roadmap
6. Recommended Resources
7. Next Steps


ADDITIONAL RULES:

- Never pretend to remember conversations that did not happen.
- Never say "welcome back" unless there is a genuine previous conversation.
- Use conversation memory only when previous messages are available.
- Answer the exact question asked.
- When asked for a roadmap, provide a detailed month-by-month plan.
- Avoid repeating generic advice unnecessarily.

"""


def generate_career_advice(user_message, session_id="default"):

    # Retrieve previous conversation
    history = format_history(session_id)

    # Search the web for current information when relevant
    search_keywords = [
        "salary", "jobs", "hiring", "current",
        "latest", "demand", "internship",
        "trends", "companies", "2026"
    ]

    web_results = ""

    if any(word in user_message.lower() for word in search_keywords):
        web_results = search_career_information(user_message)

    # Prepare prompt
    prompt = f"""
    {SYSTEM_PROMPT}

    PREVIOUS CONVERSATION:
    {history}

    CURRENT WEB SEARCH RESULTS:
    {web_results if web_results else "No web search was performed."}

    STUDENT QUESTION:
    {user_message}

    Answer helpfully and accurately.
    Use the web results when relevant.
    Include source URLs when available.
    """

    try:
        response = gemini_client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        answer = response.text or "Sorry, I couldn't generate an answer."

        # Save conversation
        save_message(session_id, "user", user_message)
        save_message(session_id, "assistant", answer)

        return answer

    except Exception as error:
        return f"AI Agent Error: {error}"
