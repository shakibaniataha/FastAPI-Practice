from fastapi import APIRouter, File, UploadFile
import shutil


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
