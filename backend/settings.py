from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    base_url: str = "/api/v1/"
    secret_key: str = "secret key"
    pg_dsn: PostgresDsn = "postgresql+asyncpg://postgres@localhost:5432/postgresusers"

    class Config:
        case_sensitive = True


settings = Settings()
