"""
test_auth.py
Kiểm thử API authentication.
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_login_success():
    """
    Kiểm tra login thành công.
    """
    response = client.post(
        "/auth/login",
        params={"username": "admin", "password": "123"}
    )

    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_fail():
    """
    Kiểm tra login thất bại.
    """
    response = client.post(
        "/auth/login",
        params={"username": "wrong", "password": "wrong"}
    )

    assert response.status_code == 401