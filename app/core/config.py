from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OPENAI_API_KEY: str = ""
    MODEL_NAME: str = "gpt-4o-mini"
    MAX_TOKENS: int = 1000
    TEMPERATURE: float = 0.8

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
