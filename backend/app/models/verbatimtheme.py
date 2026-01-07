#app/models/verbatimtheme

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.core.db import Base

class VerbatimTheme(Base):
    __tablename__ = "verbatim_theme"

    id = Column(Integer, primary_key=True)
    verbatim_id = Column(Integer, ForeignKey("verbatim.id"))
    theme_id = Column(Integer, ForeignKey("themes.id"))

    verbatim = relationship("Verbatim", back_populates="themes")
    theme = relationship("Theme", back_populates="verbatims")
