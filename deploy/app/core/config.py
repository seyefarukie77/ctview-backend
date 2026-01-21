# C:\Seye\ctview-backend\app\core\config.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "ctview backend"
    API_V1_STR: str = "/api"

    BACKEND_CORS_ORIGINS: str = "*"

    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore"
    }

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return (
            f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

settings = Settings()

def get_settings():
    return settings