from fastapi import FastAPI
from app import router as api_router

app = FastAPI(title="Minha API", version="1.0")

app.include_router(api_router)