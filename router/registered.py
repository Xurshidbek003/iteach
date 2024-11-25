from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import database
from functions.registered import create_register, update, delete
from models.registered import Register
from schemas.registered import CreateRegister

register_router = APIRouter(
    prefix="/registered",
    tags=["Register"]
)

@register_router.get("/get_register")
def get(db: Session = Depends(database)):
    return db.query(Register).all()


@register_router.post("/create_register")
def create_new_register(form: CreateRegister, db: Session = Depends(database)):
    create_register(form, db)
    raise HTTPException(200, "Amaliyiot muvafaqiyatli amalga oshirildi")


@register_router.put("/update_register")
def update_register(form: CreateRegister, register_id: int, db: Session = Depends(database)):
     update(form, register_id, db)
     raise HTTPException(200, "Amaliyiot muvafaqiyatli amalga oshirildi")


@register_router.delete("/delete_register")
def delete_register(register_id: int, db: Session = Depends(database)):
     delete(db, register_id)
     raise HTTPException(200, "Amaliyiot muvafaqiyatli amalga oshirildi")
