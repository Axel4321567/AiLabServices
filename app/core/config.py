from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "MicroAPI"
    debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8000
    mongo_uri: str = "mongodb://localhost:27017/"
    mongo_db: str = "local"
    env: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()
