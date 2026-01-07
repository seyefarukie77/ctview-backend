from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.services.analytics_service import (
    get_overview,
    get_sentiment,
    get_themes,
    get_theme_sentiment,
    get_verbatim,
)

router = APIRouter(prefix="/analytics", tags=["analytics"])

@router.get("/overview")
def overview(db: Session = Depends(get_db)):
    return get_overview(db)

@router.get("/sentiment")
def sentiment(db: Session = Depends(get_db)):
    return get_sentiment(db)

@router.get("/themes")
def themes(db: Session = Depends(get_db)):
    return get_themes(db)

@router.get("/theme-sentiment")
def theme_sentiment(db: Session = Depends(get_db)):
    return get_theme_sentiment(db)

@router.get("/verbatim")
def verbatim(db: Session = Depends(get_db)):
    return get_verbatim(db)
