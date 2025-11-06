# Kelly AI Scientist

A Streamlit web application that provides AI responses about artificial intelligence topics in analytical poetry form.

## About

Kelly is an AI chatbot that responds to questions about artificial intelligence using analytical poetry. Powered by Groq's LLaMA models, it provides educational responses that highlight both AI capabilities and limitations through creative expression.

**Key Features:**
- AI responses in poetic format
- Focus on AI education and analysis
- Clean web interface
- Powered by LLaMA 3.3 70B model

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd kelly-ai-scientist
```

2. Create virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
```
Edit `.env` and add your Groq API key:
```
GROQ_API_KEY=your_api_key_here
```

## Usage

Start the application:
```bash
streamlit run app.py
```

Open your browser and navigate to `http://localhost:8501`