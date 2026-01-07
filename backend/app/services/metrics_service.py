from sqlalchemy.orm import Session
from .. import models, schemas


def get_metrics(db: Session, limit: int = 100):
    return db.query(models.metrics.Metric).order_by(models.metrics.Metric.date.desc()).limit(limit).all()


def create_metric(db: Session, metric_in: schemas.metrics.MetricCreate):
    metric = models.metrics.Metric(**metric_in.dict())
    db.add(metric)
    db.commit()
    db.refresh(metric)
    return metric
