"""
config.py
Quản lý cấu hình hệ thống thông qua biến môi trường.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Lớp cấu hình chính của ứng dụng.

    Các biến nhạy cảm được đọc từ file .env.
    """

    PROJECT_NAME: str = "API Base Project"
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    LLM_API_KEY: str

    class Config:
        """Cấu hình đọc file môi trường."""
        env_file = ".env"


settings = Settings()