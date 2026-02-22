"""
ingestion_service.py
Module xử lý nạp dữ liệu.
"""

import os


class IngestionService:
    """
    Service xử lý ingest dữ liệu vào hệ thống.
    """

    @staticmethod
    def ingest(file_path: str) -> dict:
        """
        Kiểm tra và nạp file.
        """

        if not os.path.exists(file_path):
            raise FileNotFoundError("File not found")

        return {"message": "Ingestion successful"}