# ctview-backend / backend / app/ api / router / dashboards.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.services import dashboards_service as dashboards_service

router = APIRouter(prefix="/dashboards", tags=["dashboards"])

@router.get("/engagement-yoy")
def engagement_yoy(db: Session = Depends(get_db)):
    return dashboards_service.get_engagement_yoy(db)

@router.get("/overview")
def overview(db: Session = Depends(get_db)):
    return dashboards_service.get_overview(db)

@router.get("/sentiment")
def sentiment(db: Session = Depends(get_db)):
    return dashboards_service.get_sentiment_distribution(db)

@router.get("/department-engagement")
def department_engagement(db: Session = Depends(get_db)):
    return dashboards_service.get_engagement_by_department(db)
