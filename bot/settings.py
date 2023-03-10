from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_USER: str = "test"
    DB_PASSWORD: str = "test"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "bot"

    BOT_TOKEN: str = ""

    def db_dsn(self) -> str:
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:"
            f"{self.DB_PORT}/{self.DB_NAME}"
        )


settings = Settings()
