from fastapi import FastAPI

from db import Base, engine
from router.course import course_router
from router.opinion import opinion_router
from router.registered import register_router
from fastapi.staticfiles import StaticFiles

app = FastAPI(docs_url="/")

app.mount("/images", StaticFiles(directory="images"), name="images")

Base.metadata.create_all(bind=engine)


app.include_router(course_router)
app.include_router(opinion_router)
app.include_router(register_router)
