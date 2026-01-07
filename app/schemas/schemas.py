# unified schemas

from pydantic import BaseModel
from typing import Optional


class Overview(BaseModel):
    total_metrics: int
    latest_engagement: Optional[float]
    last_updated: Optional[str]


class YoYPoint(BaseModel):
    year: int
    value: float
    dimension: Optional[str]


class Verbatim(BaseModel):
    id: int
    text: str
    theme: Optional[str]
    sentiment: Optional[str]
    date: str


class SentimentPoint(BaseModel):
    date: str
    positive: int
    neutral: int
    negative: int


class ThemeDistribution(BaseModel):
    theme: str
    count: int
    percentage: float


class ThemeSentiment(BaseModel):
    theme: str
    positive: int
    neutral: int
    negative: int


class EngagementDim(BaseModel):
    dimension: str
    score: float
