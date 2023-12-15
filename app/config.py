from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    instancesn: str
    usernamesn: str
    passwordsn: str

    class Config:
        env_file = ".env"


settings = Settings()
