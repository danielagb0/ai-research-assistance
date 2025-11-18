import logging
from groq import Groq
from app.config import load_settings

logger = logging.getLogger("research")

settings = load_settings()
client = Groq(api_key=settings.api_key)

MODEL = "llama-3.1-8b-instant"


def analyze_question(question: str) -> str:
    """
    Clean and validate the user question.
    """
    q = question.strip()

    if not q:
        raise ValueError("Input question is empty.")

    logger.info(f"Normalized question: {q}")
    return q


def ask_llama(question: str) -> str:
    """
    Send the user question to the Llama model through Groq API
    and return the generated text.
    """
    logger.info("Sending request to Llama model...")

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a clear and concise research assistant."},
            {"role": "user", "content": question}
        ]
    )

    # Correct access: message is an object, not a dict
    answer = response.choices[0].message.content

    logger.info("Model response received.")
    return answer
