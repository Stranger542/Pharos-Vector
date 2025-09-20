import os
from pydantic import BaseSettings

class AppConfig(BaseSettings):
    APP_NAME: str = "Fake News Detection Platform"
    DEBUG: bool = True
    SECRET_KEY: str = "super-secret-key"
    DATABASE_URL: str = "sqlite:///./app.db"
    NEWSGUARD_API_KEY: str = os.getenv("NEWSGUARD_API_KEY", "")
    FACTCHECK_API_KEY: str = os.getenv("FACTCHECK_API_KEY", "")
    # Add more environment variables or settings as needed

    class Config:
        env_file = ".env"

settings = AppConfig()
