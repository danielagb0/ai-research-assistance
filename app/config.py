from pydantic import BaseModel
from dotenv import load_dotenv
import os

class Settings(BaseModel):
    api_key: str

def load_settings() -> Settings:
    load_dotenv()
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError("API_KEY no está definida en .env")

    return Settings(api_key=api_key)
