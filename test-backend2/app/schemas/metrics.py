# app/schema/metrics
from datetime import date
from pydantic import BaseModel

class MetricBase(BaseModel):
    name: str
    value: float
    date: date
    dimension: str | None = None


class MetricCreate(MetricBase):
    pass


class Metric(MetricBase):
    id: int

    model_config = {
        "from_attributes": True
    }