import logging
import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from functools import lru_cache

load_dotenv()
log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = bool(0)


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()