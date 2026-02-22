"""
file_upload.py
API xử lý upload file.
"""

import os
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends

from app.security.security import get_current_user


UPLOAD_DIRECTORY = "utils/upload_temp"

router = APIRouter(prefix="/file", tags=["File"])


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    current_user: dict = Depends(get_current_user)
):
    """
    Upload file lên server.
    Yêu cầu JWT hợp lệ.
    """

    try:
        os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

        file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)

        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)

        return {"filename": file.filename}

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="File upload failed"
        ) from exc