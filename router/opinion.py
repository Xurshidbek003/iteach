from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session

from db import database
from functions.opinion import create_opinion, update_opinion, delete_opinion, opinion_video
from models.opinion import Opinion
from schemas.opinion import CreateOpinion

opinion_router = APIRouter(
    prefix="/opinions",
    tags=["Opinions"]
)

@opinion_router.get("/get_opinion")
def get(db: Session = Depends(database)):
    return db.query(Opinion).all()


@opinion_router.post("/create_opinion")
def create_new_opinion(form: CreateOpinion, db: Session = Depends(database)):
    create_opinion(form, db)
    raise HTTPException(200, "Amaliyiot muvafaqiyatli amalga oshirildi")

@opinion_router.post('/upload-video')
def video_yuklash(ident: int = 0, file: UploadFile = File(...), db: Session = Depends(database)):
    opinion_video(ident, file, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvafaqiyatli amalga oshirildi!")

@opinion_router.put("/update_opinion")
def update_existing_opinion(ident: int, form: CreateOpinion,  db: Session = Depends(database)):
    update_opinion(ident, form, db)
    raise HTTPException(200, "Amaliyot muvafaqiyatli amalga oshirildi")

@opinion_router.delete("/delete_opinion")
def delete_existing_opinion(opinion_id: int, db: Session = Depends(database)):
     delete_opinion(opinion_id, db)
     raise HTTPException(200, "Amaliyot muvafaqiyatli amalga oshirildi")
