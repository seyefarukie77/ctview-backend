# app/model/metrics

from sqlalchemy import Column, Integer, String, Float, Date
from ..core.db import Base

from sqlalchemy import Column, Integer, String, Float, Date
from app.core.db import Base

class Metric(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    value = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    dimension = Column(String, nullable=True)
