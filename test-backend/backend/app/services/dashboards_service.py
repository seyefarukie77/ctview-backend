from sqlalchemy.orm import Session
from ..models.metrics import Metric


def get_engagement_yoy(db: Session):
    # Placeholder example aggregation
    # Replace with real YoY logic
    rows = (
        db.query(Metric.date, Metric.value)
        .order_by(Metric.date.asc())
        .all()
    )
    return [{"date": r[0].isoformat(), "value": r[1]} for r in rows]
