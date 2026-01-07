# unified backend SQLAlchemy Models
# app/models/models

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Date,
    ForeignKey,
    Float,
)
from sqlalchemy.orm import relationship

from app.core.db import Base


class Verbatim(Base):
    __tablename__ = "verbatim"

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    date = Column(Date, nullable=False)
    source = Column(String, nullable=True)

    themes = relationship("VerbatimTheme", back_populates="verbatim")
    sentiments = relationship("VerbatimSentiment", back_populates="verbatim")


class Theme(Base):
    __tablename__ = "themes"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    verbatims = relationship("VerbatimTheme", back_populates="theme")


class Sentiment(Base):
    __tablename__ = "sentiments"

    id = Column(Integer, primary_key=True)
    label = Column(String, unique=True, nullable=False)

    verbatims = relationship("VerbatimSentiment", back_populates="sentiment")


class VerbatimTheme(Base):
    __tablename__ = "verbatim_theme"

    id = Column(Integer, primary_key=True)
    verbatim_id = Column(Integer, ForeignKey("verbatim.id"))
    theme_id = Column(Integer, ForeignKey("themes.id"))

    verbatim = relationship("Verbatim", back_populates="themes")
    theme = relationship("Theme", back_populates="verbatims")


class VerbatimSentiment(Base):
    __tablename__ = "verbatim_sentiment"

    id = Column(Integer, primary_key=True)
    verbatim_id = Column(Integer, ForeignKey("verbatim.id"))
    sentiment_id = Column(Integer, ForeignKey("sentiments.id"))

    verbatim = relationship("Verbatim", back_populates="sentiments")
    sentiment = relationship("Sentiment", back_populates="verbatims")


class Engagement(Base):
    __tablename__ = "engagement"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    dimension = Column(String, nullable=True)
    year = Column(Integer, nullable=False)
    value = Column(Float, nullable=False)
