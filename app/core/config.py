from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App metadata
    APP_NAME: str = "ctview backend"
    API_V1_STR: str = "/api"

    # CORS
    BACKEND_CORS_ORIGINS: str = "*"

    # Database
    DB_USER:str
    DB_PASSWORD:str
    DB_HOST:str
    DB_PORT:int
    DB_NAME:str

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return (
            f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    model_config = {
        # no env_file in production
        "extra": "ignore"
    }

settings = Settings()

def get_settings():
    return settings
