from pydantic import BaseModel


class CreateOpinion(BaseModel):
    full_name: str
    text: str
