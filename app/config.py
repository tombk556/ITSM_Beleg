from pydantic import BaseSettings

class Settings(BaseSettings):
    instance_sn: str
    username_sn: str
    password_sn: str
    
    class Config:
        env_file = ".env"

settings = Settings()