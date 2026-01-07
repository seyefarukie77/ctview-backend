from flask import Flask, render_template, jsonify
import requests
import plotly.graph_objs as go
import plotly
import json
import os

app = Flask(__name__)

BACKEND_BASE_URL = os.getenv("BACKEND_BASE_URL", "http://localhost:8000/api")


def fetch_engagement_yoy():
    url = f"{BACKEND_BASE_URL}/dashboards/engagement-yoy"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/engagement-yoy")
def engagement_yoy_page():
    data = fetch_engagement_yoy()
    dates = [d["date"] for d in data]
    values = [d["value"] for d in data]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=values, mode="lines+markers", name="Engagement"))

    fig.update_layout(
        title="Engagement YoY",
        xaxis_title="Date",
        yaxis_title="Engagement Score",
        template="plotly_white",
    )

    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("engagement_yoy.html", graph_json=graph_json)


# Example JSON endpoint if you want to fetch chart data via JS
@app.route("/api/engagement-yoy")
def engagement_yoy_api():
    data = fetch_engagement_yoy()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
