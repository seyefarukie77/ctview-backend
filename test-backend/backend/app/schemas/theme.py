#app/schema/theme

from pydantic import BaseModel

class Theme(BaseModel):
    id: int
    name: str

    model_config = {"from_attributes": True}
