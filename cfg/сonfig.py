import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    MODE: str

    DB_DWH_HOST: str
    DB_DWH_PORT: int
    DB_DWH_USER: str
    DB_DWH_PASS: str
    DB_DWH_NAME: str

    MQ_HOST: str
    MQ_QUEUE_NAME: str

    @property
    def get_MQ_HOST(self)-> str:
        return self.MQ_HOST

    @property
    def get_MQ_QUEUE_NAME(self)-> str:
        return self.MQ_QUEUE_NAME

    @property
    def get_DB_DWH_HOST(self)-> str:
        return self.DB_DWH_HOST

    @property
    def get_DB_DWH_PORT(self) -> str:
        return str(self.DB_DWH_PORT)

    @property
    def get_DB_DWH_USER(self) -> str:
        return self.DB_DWH_USER

    @property
    def get_DB_DWH_PASS(self) -> str:
        return self.DB_DWH_PASS

    @property
    def get_DB_DWH_NAME(self) -> str:
        return self.DB_DWH_NAME

    @property
    def DATABASE_DWH_URL_psycopg(self) -> str:
        return f"postgresql+psycopg2://{self.DB_DWH_USER}:{self.DB_DWH_PASS}@{self.DB_DWH_HOST}:{self.DB_DWH_PORT}/{self.DB_DWH_NAME}"

    @classmethod
    def load_config(cls, env_file: str) -> 'Settings':
        load_dotenv(env_file)
        return cls()

    model_config = SettingsConfigDict(env_file=".env")

load_dotenv()
settings = Settings()
