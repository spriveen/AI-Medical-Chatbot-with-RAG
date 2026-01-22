import streamlit as st

# Step 1: Setup Streamlit
st.set_page_config(page_title="AI Mental Health Therapist", layout="wide")
st.title("🧠 SafeSpace - AI Mental Health Therapist")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Step 2: Chat input
user_input = st.chat_input("What is on your mind today?")

if user_input:
    # Append user message
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_input
    })

    # Dummy AI response
    fixed_dummy_response = (
        "I'm here for you. It's okay to feel this way. "
        "Would you like to talk more about what' s going on?"
    )

    st.session_state.chat_history.append({
        "role": "assistant",
        "content": fixed_dummy_response
    })

# Step 3: Display chat history
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
