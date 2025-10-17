from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(title="COPPEAD IMS API", version="0.1.0")

app.include_router(health_router, tags=["health"])
