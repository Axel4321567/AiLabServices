from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "MicroAPI"
    debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8000

    class Config:
        env_file = ".env"

settings = Settings()