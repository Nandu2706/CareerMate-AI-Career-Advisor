
import gradio as gr
from agent import generate_career_advice



def chat(message, history, request: gr.Request):

    if not message.strip():
        return "Please enter your question."

    # Give every browser session its own memory
    session_id = request.session_hash

    response = generate_career_advice(
        user_message=message,
        session_id=session_id
    )

    return response



# Create Gradio chat interface
demo = gr.ChatInterface(
    fn=chat,
    title="🚀 CareerMate - AI Career Advisor",
    description="""
    Your personal AI Career Advisor!

    Get help with:
    - Career recommendations
    - Current job trends
    - Salary information
    - Learning roadmaps
    - Interview preparation
    """,
    examples=[
        "I am a first-year BTech student. Which career should I choose?",
        "What is the current demand for Python developers in India?",
        "Create a 6-month full-stack development roadmap.",
        "What skills do I need to become an AI engineer?",
        "Give me five Python interview questions."
    ],
    
)


if __name__ == "__main__":
    print("Starting CareerMate AI Career Advisor...")

    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=False
    )
