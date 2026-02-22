"""
security.py
Module xử lý bảo mật: JWT và hash password.
"""

from datetime import datetime, timedelta
from typing import Dict

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext

from app.config import settings


# ======================
# Password hashing
# ======================

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ======================
# OAuth2 Scheme
# ======================

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


class SecurityService:
    """
    Service xử lý JWT và mật khẩu.
    """

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Mã hóa mật khẩu.
        """
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """
        Kiểm tra mật khẩu.
        """
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def create_access_token(data: Dict) -> str:
        """
        Tạo JWT access token.
        """
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        to_encode.update({"exp": expire})

        return jwt.encode(
            to_encode,
            settings.SECRET_KEY,
            algorithm=settings.ALGORITHM
        )

    @staticmethod
    def decode_token(token: str) -> Dict:
        """
        Giải mã JWT token.
        """
        try:
            return jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=[settings.ALGORITHM]
            )
        except JWTError as exc:
            raise ValueError("Invalid token") from exc


# ======================
# Dependency Function
# ======================

def get_current_user(token: str = Depends(oauth2_scheme)) -> Dict:
    """
    Dependency kiểm tra JWT hợp lệ.
    """
    try:
        payload = SecurityService.decode_token(token)
        return payload
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        ) from exc