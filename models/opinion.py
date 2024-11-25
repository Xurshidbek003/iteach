from db import Base
from sqlalchemy import Column, String, Integer


class Opinion(Base):
    __tablename__ = 'opinion'
    id = Column(Integer, primary_key=True, autoincrement=True)
    video = Column(String(255))
    full_name = Column(String(255))
    text = Column(String(255))