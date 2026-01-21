# app/api/router/metrics

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.schemas.metrics import Metric, MetricCreate   # Pydantic models
from app.services import metrics_service

router = APIRouter(prefix="/metrics", tags=["metrics"])


@router.get("/", response_model=list[Metric])
def read_metrics(limit: int = 100, db: Session = Depends(get_db)):
    return metrics_service.get_metrics(db, limit=limit)


@router.post("/", response_model=Metric, status_code=status.HTTP_201_CREATED)
def create_metric(metric_in: MetricCreate, db: Session = Depends(get_db)):
    return metrics_service.create_metric(db, metric_in)
