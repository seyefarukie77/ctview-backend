#app/models/verbatim

from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.core.db import Base

class Verbatim(Base):
    __tablename__ = "verbatim"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    date = Column(Date, nullable=False)
    source = Column(String, nullable=True)  # e.g. survey, review, chat, etc.

    # relationships
    themes = relationship("VerbatimTheme", back_populates="verbatim")
    sentiments = relationship("VerbatimSentiment", back_populates="verbatim")
