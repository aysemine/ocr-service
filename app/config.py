from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    FILE_DIR: str 
    OPENAI_API_KEY: str | None = None

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
