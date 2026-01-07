# app/schemas/sentiment

from pydantic import BaseModel

class Sentiment(BaseModel):
    id: int
    label: str

    model_config = {"from_attributes": True}
