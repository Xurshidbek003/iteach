from pydantic import BaseModel


class CreateRegister(BaseModel):
    name: str
    phone_num: str
