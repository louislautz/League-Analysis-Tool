from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "LoL Analysis API"
    environment: str = "development"
    database_url: str = "sqlite:///./data/lol_analysis.db"
    riot_api_key: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )
    


settings = Settings()