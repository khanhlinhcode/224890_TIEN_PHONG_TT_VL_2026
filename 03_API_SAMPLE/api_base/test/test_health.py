"""
test_health.py
Kiểm thử API health check.
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    """
    Kiểm tra endpoint health.
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"