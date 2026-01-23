# ctview-backend / backend / app/ services / dashboards_service.py
from sqlalchemy import text
from sqlalchemy.orm import Session

def get_overview(db: Session):
    # Overall averages
    overview_query = text("""
        SELECT
            AVG(employee_net_promoter_score) AS avg_nps,
            AVG(CASE WHEN employee_net_promoter_score >= 9 THEN 1 ELSE 0 END) * 100 AS promoters,
            AVG(CASE WHEN employee_net_promoter_score <= 6 THEN 1 ELSE 0 END) * 100 AS detractors
        FROM employee_feedback;
    """)

    row = db.execute(overview_query).mappings().one()

    promoters = float(row["promoters"] or 0)
    detractors = float(row["detractors"] or 0)

    # NPS formula: %Promoters - %Detractors
    nps = promoters - detractors

    # Fake delta for now (you can compute real period-over-period later)
    nps_delta = 3.2

    return {
        "nps": round(nps, 1),
        "nps_delta": nps_delta,
        "promoters": round(promoters, 1),
    }

def get_engagement_yoy(db: Session):
    """
    Returns year-over-year average engagement score.
    Example output:
    [
        {"year": 2023, "avg_engagement": 6.91},
        {"year": 2024, "avg_engagement": 7.02},
        {"year": 2025, "avg_engagement": 7.10}
    ]
    """

    query = text("""
        SELECT
            survey_year,
            AVG(engagement_score) AS avg_engagement
        FROM employee_feedback
        GROUP BY survey_year
        ORDER BY survey_year ASC;
    """)

    rows = db.execute(query).mappings().all()

    return [
        {
            "year": int(r["survey_year"]),
            "avg_engagement": float(r["avg_engagement"] or 0)
        }
        for r in rows
    ]

def get_sentiment_distribution(db: Session):
    query = text("""
        SELECT sentiment, COUNT(*) AS count
        FROM employee_feedback
        GROUP BY sentiment
        ORDER BY count DESC;
    """)
    rows = db.execute(query).mappings().all()

    return [
        {"sentiment": r["sentiment"], "count": int(r["count"])}
        for r in rows
    ]

def get_engagement_by_department(db: Session):
    query = text("""
        SELECT department, AVG(engagement_score) AS avg_engagement
        FROM employee_feedback
        GROUP BY department
        ORDER BY avg_engagement DESC;
    """)
    rows = db.execute(query).mappings().all()

    return [
        {"department": r["department"], "avg_engagement": float(r["avg_engagement"] or 0)}
        for r in rows
    ]

