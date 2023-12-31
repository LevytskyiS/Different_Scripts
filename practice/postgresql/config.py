from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # model_config = SettingsConfigDict(
    #     env_file="practice/postgresql/.env", env_file_encoding="utf-8"
    # )
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    HOST: str = "host"
    USER: str = "user"
    DB: str = "db"
    PASSWORD: str = "password"
    URL: str = "url"


settings = Settings(_env_file="practice/postgresql/.env", _env_file_encoding="utf-8")
# settings = Settings(_env_file=".env", _env_file_encoding="utf-8")
