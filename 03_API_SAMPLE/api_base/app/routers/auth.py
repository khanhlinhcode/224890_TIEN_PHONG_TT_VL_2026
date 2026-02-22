"""
auth.py
API xác thực người dùng theo chuẩn OAuth2 password flow.
"""

from fastapi import APIRouter, HTTPException, Form
from app.security.security import SecurityService

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...)
):
    """
    API đăng nhập hệ thống.
    Trả về JWT theo chuẩn OAuth2.
    """

    if username != "admin" or password != "123":
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = SecurityService.create_access_token({"sub": username})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }