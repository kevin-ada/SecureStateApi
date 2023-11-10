from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_type: str
    database_user: str
    database_password: str
    database_host:str
    database_name:str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()
