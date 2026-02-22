"""
llm_service.py
Module xử lý tương tác với LLM.
"""

import requests
from app.config import settings


class LLMService:
    """
    Service gọi API LLM.
    """

    @staticmethod
    def ask(prompt: str) -> dict:
        """
        Gửi câu hỏi lên LLM và nhận phản hồi.
        """

        headers = {
            "Authorization": f"Bearer {settings.LLM_API_KEY}"
        }

        try:
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json={
                    "model": "gpt-4o-mini",
                    "messages": [
                        {"role": "user", "content": prompt}
                    ]
                }
            )
            response.raise_for_status()
            return response.json()

        except requests.RequestException as exc:
            raise RuntimeError("LLM API request failed") from exc