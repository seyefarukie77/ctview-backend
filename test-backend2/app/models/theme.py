# app/models/theme
from sqlalchemy import Column, Integer, String
from app.core.db import Base

class Theme(Base):
    __tablename__ = "themes"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)