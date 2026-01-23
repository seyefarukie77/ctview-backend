# ctview-backend/ backend / app / main.py

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.api.router import analytics
from app.api.router import dashboards
from app.core.db import get_db
from app.services import dashboards_service as dashboards_service

app = FastAPI(title="CTVIEW Dashboard")
templates = Jinja2Templates(directory="app/templates")

# Routers MUST be included after app is created
app.include_router(analytics.router)
app.include_router(dashboards.router)

@app.get("/", response_class=HTMLResponse)
async def ctview_dashboard(request: Request):
    db = next(get_db())

    overview = dashboards_service.get_overview(db)

    context = {
        "request": request,
        "last_updated": "2026-01-07 09:00",
        "overview": overview,
        "sentiment": None,
        "themes": None,
        "verbatim": None,
        "overview_chart": None,
        "sentiment_chart": None,
    }

    return templates.TemplateResponse("dashboard.html", context)