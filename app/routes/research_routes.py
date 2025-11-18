from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.research import analyze_question, ask_llama

router = APIRouter()


class QuestionPayload(BaseModel):
    question: str


@router.post("/ask")
async def ask(payload: QuestionPayload):
    """
    FastAPI endpoint that receives a question and returns Llama's answer.
    """
    try:
        clean_q = analyze_question(payload.question)
        answer = ask_llama(clean_q)
        return {"answer": answer}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")
