from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Получить секрет'

    class Config:
        env_file = '../.env'


settings = Settings()
