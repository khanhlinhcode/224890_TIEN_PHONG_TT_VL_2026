"""
helpers.py
Các hàm tiện ích chung cho ứng dụng.
"""


def format_response(success: bool, message: str, data=None) -> dict:
    """
    Chuẩn hóa response trả về.
    """
    return {
        "success": success,
        "message": message,
        "data": data
    }