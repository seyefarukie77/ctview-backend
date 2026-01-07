# app/models/verbatimsentiment

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.core.db import Base

class VerbatimSentiment(Base):
    __tablename__ = "verbatim_sentiment"

    id = Column(Integer, primary_key=True)
    verbatim_id = Column(Integer, ForeignKey("verbatim.id"))
    sentiment_id = Column(Integer, ForeignKey("sentiments.id"))

    verbatim = relationship("Verbatim", back_populates="sentiments")
    sentiment = relationship("Sentiment", back_populates="verbatims")
