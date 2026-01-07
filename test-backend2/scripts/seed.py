# AWS EB
# Backend/scripts/seed.py
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sqlalchemy.orm import Session
from backend.app.core.db import SessionLocal
from backend.app.models import Sentiment, Theme

from app.models.models import (
    Verbatim,
    Theme,
    Sentiment,
    VerbatimTheme,
    VerbatimSentiment,
)
from backend.app.core.db import SessionLocal
from datetime import date

def seed():
    db = SessionLocal()

    # Sentiments
    sentiments = ["positive", "neutral", "negative"]
    sentiment_objs = {}
    for s in sentiments:
        obj = Sentiment(label=s)
        db.add(obj)
        sentiment_objs[s] = obj

    # Themes
    themes = ["Delivery", "Pricing", "Customer Service", "Product Quality"]
    theme_objs = {}
    for t in themes:
        obj = Theme(name=t)
        db.add(obj)
        theme_objs[t] = obj

    # Verbatim examples
    verbatims = [
        ("The delivery was fast and smooth", date(2026, 1, 1), "survey", "Delivery", "positive"),
        ("Pricing is too high for what you get", date(2026, 1, 2), "survey", "Pricing", "negative"),
        ("Customer service was okay, nothing special", date(2026, 1, 3), "survey", "Customer Service", "neutral"),
        ("Product quality exceeded expectations", date(2026, 1, 4), "survey", "Product Quality", "positive"),
    ]

    for text, d, src, theme, sentiment in verbatims:
        v = Verbatim(text=text, date=d, source=src)
        db.add(v)
        db.flush()

        db.add(VerbatimTheme(verbatim_id=v.id, theme_id=theme_objs[theme].id))
        db.add(VerbatimSentiment(verbatim_id=v.id, sentiment_id=sentiment_objs[sentiment].id))

    db.commit()
    db.close()
    print("Seed complete.")