"""
run_api.py
Script chạy ứng dụng FastAPI.
"""

import uvicorn


if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)