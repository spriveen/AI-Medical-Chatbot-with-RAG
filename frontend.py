import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000/ask"

# Step 1: Setup Streamlit
st.set_page_config(page_title="AI Mental Health Therapist", layout="wide")
st.title("🧠 SafeSpace - AI Mental Health Therapist")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Step 2: Chat input
user_input = st.chat_input("What is on your mind today?")

if user_input:
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_input
    })

    try:
        fixed_dummy_response_from_backend = requests.post(
            BACKEND_URL,
            json={"message": user_input}
        )

        bot_reply = fixed_dummy_response_from_backend.json().get(
            "response", "No response from backend"
        )

    except Exception as e:
        bot_reply = "Backend not running"

    st.session_state.chat_history.append({
        "role": "assistant",
        "content": bot_reply
    })

# Step 3: Display chat history
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
