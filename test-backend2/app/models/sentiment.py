#app/models/sentiments
from sqlalchemy import Column, Integer, String
from app.core.db import Base


class Sentiment(Base):
    __tablename__ = "sentiments"

    id = Column(Integer, primary_key=True)
    label = Column(String, unique=True, nullable=False)


class Sentiment(Base):
    __tablename__ = "sentiments"

    id = Column(Integer, primary_key=True)
    label = Column(String, unique=True, nullable=False)

class Sentiment(Base):
    __tablename__ = "sentiments"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String, unique=True, nullable=False)  # positive, neutral, negative

    verbatims = relationship("VerbatimSentiment", back_populates="sentiment")
