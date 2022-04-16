from fastapi import APIRouter, File, UploadFile, HTTPException, status
from fastapi.responses import FileResponse
import shutil
import os


router = APIRouter(prefix="/file", tags=["file"])


@router.post("/file")
def get_file(file: bytes = File(...)):
    content = file.decode("utf-8")
    lines = content.split("\n")
    return {"lines": lines}


@router.post("/uploadfile")
def get_uploadfile(uploadfile: UploadFile = File(...)):
    path = f"files/{uploadfile.filename}"
    with open(path, "w+b") as buffer:
        shutil.copyfileobj(uploadfile.file, buffer)

    return {"address": path, "file_type": uploadfile.content_type}


@router.get("/download/{name}", response_class=FileResponse)
def download_file(name: str):
    file_path = f"files/{name}"

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="file not found"
        )

    return file_path
