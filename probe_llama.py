from groq import Groq
from config import load_settings

def main():
    settings = load_settings()
    client = Groq(api_key=settings.api_key)

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "user", "content": "Decime en una frase corta que este proyecto funciona correctamente."}
        ]
    )

    print(response.choices[0].message["content"])

if __name__ == "__main__":
    main()
