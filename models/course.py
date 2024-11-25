from db import Base
from sqlalchemy import Column, String, Integer


class Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=True)
    period = Column(String(255), nullable=True)
    teacher = Column(String(255), nullable=True)
    lesson_count = Column(Integer, nullable=True)
    language = Column(String(255), nullable=True)
    image = Column(String(255), nullable=True)
    video = Column(String(255), nullable=True)


