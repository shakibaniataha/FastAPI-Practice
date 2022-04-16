from fastapi import APIRouter, File


router = APIRouter(prefix="/file", tags=["file"])


@router.post("/upload")
def upload_file(file: bytes = File(...)):
    content = file.decode('utf-8')
    lines = content.split('\n')
    return {'lines': lines}
