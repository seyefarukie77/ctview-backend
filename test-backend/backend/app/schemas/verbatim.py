#app/schema/Verbatim

from datetime import date
from pydantic import BaseModel

class VerbatimBase(BaseModel):
    text: str
    date: date
    source: str | None = None

class VerbatimCreate(VerbatimBase):
    themes: list[str] = []
    sentiments: list[str] = []

class Verbatim(VerbatimBase):
    id: int
    themes: list[str]
    sentiments: list[str]

    model_config = {"from_attributes": True}
