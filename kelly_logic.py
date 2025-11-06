"""
Kelly Logic Module - AI responses in poetic form
"""

from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
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
