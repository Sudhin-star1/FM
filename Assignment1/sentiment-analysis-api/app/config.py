from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_name: str = "distilbert-base-uncased-finetuned-sst-2-english"

    class Config:
        env_file=".env"

settings = Settings()