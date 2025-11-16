from fastapi import FastAPI
from pydantic import BaseModel
from research import analyze_question, ask_llama

app = FastAPI()

class AskRequest(BaseModel):
    question: str

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/ask")
def ask(request: AskRequest):
    question = analyze_question(request.question)
    answer = ask_llama(question)
    return {"answer": answer}
