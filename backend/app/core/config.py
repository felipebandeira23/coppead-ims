from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://ims_user:ims_pwd_strong@mysql:3306/coppead_ims"
    SECRET_KEY: str = "change-me"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = "backend/.env"
        extra = "ignore"

settings = Settings()

