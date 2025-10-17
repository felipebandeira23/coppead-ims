from fastapi import APIRouter
from app.core.db import ping_db

router = APIRouter()

@router.get("/healthz")
def healthz():
    # testa conexão com DB (vai lançar exceção se falhar)
    ping_db()
    return {"status": "ok"}
