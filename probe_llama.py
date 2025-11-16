from groq import Groq
from config import load_settings

def main():
    settings = load_settings()
    client = Groq(api_key=settings.api_key)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": "Confirmá en una frase que el proyecto está funcionando."}
        ]
    )
    print("Prompt enviado")
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
