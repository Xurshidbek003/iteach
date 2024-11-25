from fastapi import HTTPException, UploadFile, File, Depends
from sqlalchemy.orm import Session

from db import database
from models.course import Course
from utils.image_save import save_file


def course_image(ident, file: UploadFile = File(...), db: Session = Depends(database)):
    image_filename = save_file(file)
    course = db.query(Course).filter(Course.id == ident).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course topilmadi")
    course.image = image_filename
    db.commit()


def course_video(ident, file: UploadFile = File(...), db: Session = Depends(database)):
    video_filename = save_file(file)
    course = db.query(Course).filter(Course.id == ident).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course topilmadi")
    course.video = video_filename
    db.commit()

def create_course(form, db):
    new_course = Course(
        title=form.title,
        period=form.period,
        teacher=form.teacher,
        lesson_count=form.lesson_count,
        language=form.language
    )
    db.add(new_course)
    db.commit()

def update_course(ident, form, db):
    course = db.query(Course).filter(Course.id == ident).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course topilmadi")
    db.query(Course).filter(Course.id == ident).update({
        Course.title: form.title,
        Course.period: form.period,
        Course.lesson_count: form.lesson_count,
        Course.language: form.language,
    })
    db.commit()
    db.refresh(course)


def delete_course(ident, db):
    course = db.query(Course).filter(Course.id == ident).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course topilmadi")
    db.delete(course)
    db.commit()
