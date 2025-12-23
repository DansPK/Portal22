from fastapi import FastAPI
from app.api.v1.router import router as v1_router

app = FastAPI(title="Portal22 API", version="0.1.0")

app.include_router(v1_router, prefix="/api/v1")

@app.get("/health")
def health():
    return {"status": "ok"}
