
# Conversation Memory

conversation_history = {}

MAX_HISTORY = 10


def get_history(session_id):
    """Retrieve previous conversation messages."""

    if session_id not in conversation_history:
        conversation_history[session_id] = []

    return conversation_history[session_id]


def save_message(session_id, role, message):
    """Save a message to conversation memory."""

    history = get_history(session_id)

    history.append({
        "role": role,
        "content": message
    })

    # Keep only the latest 10 messages
    conversation_history[session_id] = history[-MAX_HISTORY:]


def clear_memory(session_id):
    """Clear conversation history."""

    conversation_history[session_id] = []


def format_history(session_id):
    """Convert conversation history into text."""

    history = get_history(session_id)

    if not history:
        return "No previous conversation."

    formatted = []

    for message in history:
        role = message["role"].upper()
        content = message["content"]

        formatted.append(f"{role}: {content}")

    return "\n".join(formatted)
