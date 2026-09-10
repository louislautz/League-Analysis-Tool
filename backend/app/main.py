from fastapi import FastAPI

from app.FastAPI.routes.players import router as players_router
from app.FastAPI.routes.matches import router as matches_router
from app.core.config import settings
from app.database.base import Base
from app.database.session import engine

import app.database.models


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
)

Base.metadata.create_all(bind=engine)

app.include_router(players_router)
app.include_router(matches_router)


@app.get("/health")
def health():
    return {"status": "ok"}