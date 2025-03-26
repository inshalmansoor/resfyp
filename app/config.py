from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    mongodb_uri: str
    openai_api_key: str
    # add other keys as needed

    class Config:
        env_file = ".env"

settings = Settings()
