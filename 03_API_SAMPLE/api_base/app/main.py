"""
main.py
Khởi tạo FastAPI application.
"""

from fastapi import FastAPI

from app.config import settings
from app.routers import auth, base, file_upload

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(auth.router)
app.include_router(base.router)
app.include_router(file_upload.router)