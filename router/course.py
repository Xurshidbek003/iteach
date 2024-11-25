from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from sqlalchemy.orm import Session

from db import database
from functions.course import create_course, course_image, delete_course, course_video, update_course
from models.course import Course
from schemas.course import CreateCourse, UpdateCourse

course_router = APIRouter(
    prefix="/courses",
    tags=["Course operation"]
)


@course_router.get('/get')
def get_courses(db: Session = Depends(database)):
    courses = db.query(Course).all()
    if not courses:
        raise HTTPException(status_code=404, detail="No courses found")
    return courses



@course_router.post("/create_course")
async def course_yaratish(form: CreateCourse, db: Session = Depends(database)):
    create_course(form, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@course_router.post('/upload-image')
def rasm_yuklash(ident: int = 0, file: UploadFile = File(...), db: Session = Depends(database)):
    course_image(ident, file, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvafaqiyatli amalga oshirildi!")

@course_router.post('/upload-video')
def video_yuklash(ident: int = 0, file: UploadFile = File(...), db: Session = Depends(database)):
    course_video(ident, file, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvafaqiyatli amalga oshirildi!")

@course_router.put("/update_course")
def kursni_tahrirlash(ident: int, form: UpdateCourse, db: Session = Depends(database)):
    update_course(ident, form, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@course_router.delete("/delete")
def kursni_ochirish(ident: int, db: Session = Depends(database)):
    delete_course(ident, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")
