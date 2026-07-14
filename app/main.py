from fastapi import FastAPI
from app.webhook import router

app = FastAPI(
    title="AI WhatsApp Assistant",
    version="1.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "status": "running",
        "service": "AI WhatsApp Assistant"
    }