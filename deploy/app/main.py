from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.api.router import analytics

app = FastAPI(title="CTVIEW Dashboard")
templates = Jinja2Templates(directory="app/templates")

app.include_router(analytics.router)

@app.get("/", response_class=HTMLResponse)
async def ctview_dashboard(request: Request):
    context = {
        "request": request,
        "last_updated": "2026-01-07 09:00",
        "overview": None,
        "sentiment": None,
        "themes": None,
        "verbatim": None,
        "overview_chart": None,
        "sentiment_chart": None,
    }
    return templates.TemplateResponse("dashboard.html", context)
