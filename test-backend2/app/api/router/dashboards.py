from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.services import dashboards_service


router = APIRouter(prefix="/dashboards", tags=["dashboards"])


@router.get("/engagement-yoy")
def engagement_yoy(db: Session = Depends(get_db)):
    return dashboards_service.get_engagement_yoy(db)
