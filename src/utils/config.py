import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load variables from the .env file
load_dotenv()

class Settings(BaseSettings):
    """Application configuration and environment variables."""
    FRED_API_KEY: str = os.getenv("FRED_API_KEY", "")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
