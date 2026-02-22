API Base Project

1. Giới thiệu

Dự án được xây dựng bằng FastAPI với kiến trúc module hóa, tuân thủ:
	•	Single Responsibility Principle
	•	Clean Code
	•	JWT Authentication
	•	Environment Variable Security

⸻

2. Công nghệ sử dụng
	•	Python 3.11+
	•	FastAPI
	•	JWT (python-jose)
	•	SQLAlchemy
	•	Pytest
	•	Requests

⸻

3. Cấu trúc hệ thống
api_base/
 ├── app/
 ├── chatbot/
 ├── ingestion/
 ├── utils/
 ├── test/
 

 4. Chức năng chính
	•	Authentication (JWT)
	•	Health Check
	•	File Upload
	•	Chatbot Service
	•	Data Ingestion

5. Bảo mật
	•	SECRET_KEY lưu trong .env
	•	LLM_API_KEY lưu trong .env
	•	Không hard-code key
	•	Frontend sử dụng JWT

6. Cách chạy hệ thống

    pip install -r requirements.txt
    python run_api.py
    http://127.0.0.1:8000/docs

7. Chạy kiểm thử
    pytest