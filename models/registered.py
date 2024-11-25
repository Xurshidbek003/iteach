from db import Base
from sqlalchemy import Column, String, Integer


class Register(Base):
    __tablename__ = 'registered'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    phone_num = Column(String(255))