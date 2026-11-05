
from memory import save_message, format_history

session = "student_001"

save_message(session, "user", "I am a first-year BTech student.")
save_message(session, "assistant", "Great! What career interests you?")
save_message(session, "user", "I want to become a Python developer.")

print(format_history(session))
