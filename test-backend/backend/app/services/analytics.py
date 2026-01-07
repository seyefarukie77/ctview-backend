# app/services/analytics

from datetime import date
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models import Verbatim, Theme, Sentiment, VerbatimTheme, VerbatimSentiment


def get_overview(db: Session):
    total_metrics = db.query(func.count(Verbatim.id)).scalar() or 0

    latest = (
        db.query(Verbatim.date)
        .order_by(Verbatim.date.desc())
        .limit(1)
        .scalar()
    )

    sentiment_trend = (
        db.query(
            Verbatim.date.label("date"),
            func.avg(
                func.coalesce(
                    func.nullif(Sentiment.label, ''),  # adapt to your scheme
                    'neutral'
                )
            ).label("score")
        )
        .join(VerbatimSentiment, Verbatim.id == VerbatimSentiment.verbatim_id)
        .join(Sentiment, Sentiment.id == VerbatimSentiment.sentiment_id)
        .group_by(Verbatim.date)
        .order_by(Verbatim.date)
        .all()
    )

    # you’ll likely map sentiment labels (positive/neutral/negative) to numeric scores in a table or in code

    return {
        "total_metrics": total_metrics,
        "latest_engagement": None,  # fill from engagement data if you have it
        "last_updated": latest.isoformat() if latest else None,
        "sentiment_trend": [
            {"date": row.date.isoformat(), "score": float(row.score)}
            for row in sentiment_trend if row.score is not None
        ],
    }


def get_sentiment_series(db: Session):
    # returns [{date, positive, neutral, negative}]
    rows = (
        db.query(
            Verbatim.date.label("date"),
            func.sum(func.case((Sentiment.label == "positive", 1), else_=0)).label("positive"),
            func.sum(func.case((Sentiment.label == "neutral", 1), else_=0)).label("neutral"),
            func.sum(func.case((Sentiment.label == "negative", 1), else_=0)).label("negative"),
        )
        .join(VerbatimSentiment, Verbatim.id == VerbatimSentiment.verbatim_id)
        .join(Sentiment, Sentiment.id == VerbatimSentiment.sentiment_id)
        .group_by(Verbatim.date)
        .order_by(Verbatim.date)
        .all()
    )

    return [
        {
            "date": row.date.isoformat(),
            "positive": int(row.positive),
            "neutral": int(row.neutral),
            "negative": int(row.negative),
        }
        for row in rows
    ]


def get_theme_distribution(db: Session):
    rows = (
        db.query(
            Theme.name.label("theme"),
            func.count(VerbatimTheme.id).label("count"),
        )
        .join(VerbatimTheme, Theme.id == VerbatimTheme.theme_id)
        .group_by(Theme.name)
        .order_by(func.count(VerbatimTheme.id).desc())
        .all()
    )
    total = sum(r.count for r in rows) or 1

    return [
        {
            "theme": r.theme,
            "count": int(r.count),
            "percentage": r.count / total,
        }
        for r in rows
    ]


def get_theme_sentiment_matrix(db: Session):
    rows = (
        db.query(
            Theme.name.label("theme"),
            Sentiment.label.label("sentiment"),
            func.count(Verbatim.id).label("count"),
        )
        .join(VerbatimTheme, Theme.id == VerbatimTheme.theme_id)
        .join(Verbatim, Verbatim.id == VerbatimTheme.verbatim_id)
        .join(VerbatimSentiment, Verbatim.id == VerbatimSentiment.verbatim_id)
        .join(Sentiment, Sentiment.id == VerbatimSentiment.sentiment_id)
        .group_by(Theme.name, Sentiment.label)
        .all()
    )

    matrix = {}
    for r in rows:
        matrix.setdefault(r.theme, {"positive": 0, "neutral": 0, "negative": 0})
        matrix[r.theme][r.sentiment] = int(r.count)

    return [
        {
            "theme": theme,
            "positive": vals["positive"],
            "neutral": vals["neutral"],
            "negative": vals["negative"],
        }
        for theme, vals in matrix.items()
    ]
