from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="practice/mysql/.env", env_file_encoding="utf-8"
    )
    HOST: str = "host"
    PORT: int = 1234
    USER: str = "user"
    PASSWORD: str = "password"
    DB: str = "db"


settings = Settings(_env_file="practice/mysql/.env", _env_file_encoding="utf-8")
