from groq import Groq
from config import load_settings

settings = load_settings()
client = Groq(api_key=settings.api_key)

MODEL = "llama-3.1-8b-instant"

def analyze_question(question: str) -> str:
    """
    Limpia y normaliza la pregunta del usuario.
    Esta función se irá expandiendo luego (detección de intención, clasificación, etc.)
    """
    q = question.strip()
    if not q:
        raise ValueError("La pregunta está vacía.")
    return q

def ask_llama(question: str) -> str:
    """
    Envía la pregunta al modelo Llama en Groq y devuelve la respuesta limpia.
    """
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "Sos un asistente de investigación claro y directo."},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message["content"]
