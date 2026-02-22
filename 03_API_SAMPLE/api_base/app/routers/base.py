"""
base.py
API kiểm tra trạng thái hệ thống.
"""

from fastapi import APIRouter

router = APIRouter(tags=["System"])


@router.get("/health")
def health_check():
    """
    Kiểm tra server đang hoạt động.
    """
    return {"status": "ok"}