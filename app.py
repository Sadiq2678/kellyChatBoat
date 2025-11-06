"""
Kelly - The AI Scientist Poet
Streamlit Chatbot UI
"""

import streamlit as st
from kelly_logic import chat_with_kelly

st.set_page_config(page_title="Kelly - AI Scientist Poet", page_icon="🧠", layout="centered")

st.title("🧠 Kelly - The AI Scientist Poet")
st.write("Ask anything about AI. Kelly replies as analytical poetic scientist.")

# Session state to store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# user input
prompt = st.chat_input("Ask Kelly about AI...")

if prompt:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message instantly
    with st.chat_message("user"):
        st.markdown(prompt)

    # Kelly response
    with st.chat_message("assistant"):
        with st.spinner("Kelly is composing poetic analysis..."):
            try:
                output = chat_with_kelly(prompt)
            except Exception as e:
                output = f"Error occurred: {e}"
        
        st.markdown(output)

    # store assistant reply
    st.session_state.messages.append({"role": "assistant", "content": output})
