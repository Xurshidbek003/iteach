import shutil
from fastapi import UploadFile
from fastapi import HTTPException


def save_file(image: UploadFile):
    if not image.filename.endswith((".jpg", ".png", ".jpeg", ".gif", ".heif", ".mp4")):
        raise HTTPException(400, "Yuklangan fayl formati noto'g'ri !!!")
    file_location = f"{image.filename}"
    with open(file_location, "wb") as f:
        shutil.copyfileobj(image.file, f)
    return file_location
