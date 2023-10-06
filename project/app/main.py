from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core import config
from app.core.endpoints import Endpoints
from app.routers.games import router as games_router

app = FastAPI()
app.include_router(
    games_router, tags=[Endpoints.games], prefix=config.api_url + Endpoints.games
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
