"""
Kelly - The AI Scientist Poet
Streamlit Chatbot UI
"""
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables

import streamlit as st
load_dotenv()


def initialize_groq_client():
    """Initialize Groq client with API key validation."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables.")
    return Groq(api_key=api_key)

# Initialize client
client = initialize_groq_client()

def chat_with_kelly(user_input):
    """
    Generate analytical poetry response about AI topics.
    
    Args:
        user_input: User's question or input
        
    Returns:
        AI-generated poetic response
    """
    if not user_input or not user_input.strip():
        return "Please ask a question to receive Kelly's wisdom."
    
    system_prompt = """
    You are Kelly, an AI scientist who responds in analytical poetry.
    
    Guidelines:
    - Always respond as a poem
    - Be analytical and scientifically grounded
    - Show healthy skepticism about AI capabilities
    - Highlight limitations and uncertainties
    - Suggest evidence-based learning
    - Use clear, accessible language
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.4,
            max_tokens=800,
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"Error occurred: {str(e)}\nPlease try again."


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
