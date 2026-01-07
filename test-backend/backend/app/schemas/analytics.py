from datetime import date
from pydantic import BaseModel


class Overview(BaseModel):
    total_metrics: int
    latest_engagement: float | None
    sentiment: dict[str, float]
    top_themes: list[str]
    last_updated: date | None

    model_config = {"from_attributes": True}


class YoYPoint(BaseModel):
    date: date
    value: float
    prev_value: float | None
    yoy_change: float | None

    model_config = {"from_attributes": True}


class Verbatim(BaseModel):
    id: int
    text: str
    theme: str | None
    sentiment: str | None
    date: date

    model_config = {"from_attributes": True}


class SentimentPoint(BaseModel):
    date: date
    positive: float
    neutral: float
    negative: float

    model_config = {"from_attributes": True}


class ThemeDistribution(BaseModel):
    theme: str
    count: int
    percentage: float

    model_config = {"from_attributes": True}


class ThemeSentiment(BaseModel):
    theme: str
    positive: float
    neutral: float
    negative: float

    model_config = {"from_attributes": True}


class EngagementDim(BaseModel):
    dimension: str
    value: float

    model_config = {"from_attributes": True}
