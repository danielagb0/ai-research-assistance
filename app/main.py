from fastapi import FastAPI
import uvicorn
from app.routes.research_routes import router as research_router

app = FastAPI()

# Register research endpoints
app.include_router(research_router)

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
