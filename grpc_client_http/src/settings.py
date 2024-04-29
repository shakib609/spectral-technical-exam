from fastapi import FastAPI
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ALLOWED_ORIGINS: list[str] = ["*"]

    GRPC_SERVER_HOST: str = "localhost"
    GRPC_SERVER_PORT: str = "50051"


settings = Settings()
