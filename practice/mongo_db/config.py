from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="practice/mongo_db/.env", env_file_encoding="utf-8"
    )
    USERNAME_MONGO: str = "user"
    PASSWORD_MONGO: str = "password"
    CLUSTER_MONGO: str = "cluster"


settings = Settings(_env_file="practice/mongo_db/.env", _env_file_encoding="utf-8")
