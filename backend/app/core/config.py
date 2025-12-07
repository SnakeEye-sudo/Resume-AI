from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Resume AI"
    DATABASE_URL: str = "postgresql://user:password@localhost/resume_ai_db"  # Default, need update
    
    class Config:
        env_file = ".env"

settings = Settings()
