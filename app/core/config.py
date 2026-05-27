from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    openai_api_key: str | None = None
    app_env: str = "development"

    class Config:
        env_file = ".env"


settings = Settings()