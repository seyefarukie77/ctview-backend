ctview/
│
├── backend/                     # FastAPI backend (already mostly there)
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   │   ├── analytics.py
│   │   │   ├── dashboards.py
│   │   │   └── metrics.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── db.py
│   │   ├── models/
│   │   ├── schemas/
│   │   └── services/
│   │       ├── metrics_service.py
│   │       └── dashboards_service.py
│   ├── requirements.txt
│   ├── Procfile                 # For EB (backend)
│   └── .ebextensions/
│       └── 01_backend.config
│
├── frontend/                    # New Flask + Plotly frontend
│   ├── app.py
│   ├── requirements.txt
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html           # Overview / landing
│   │   ├── engagement_yoy.html  # Engagement YoY page
│   │   ├── verbatim.html        # Verbatim explorer
│   │   ├── sentiment.html       # Sentiment distribution
│   │   ├── themes.html          # Theme distribution
│   │   ├── theme_sentiment.html # Theme × Sentiment matrix
│   │   └── engagement_dim.html  # Engagement by dimension
│   └── static/
│       ├── css/
│       │   └── styles.css
│       └── js/
│           └── charts.js
│
├── infra/                       # Optional: IaC / DB migrations etc.
│   └── (CloudFormation / Terraform / Alembic)
│
└── README.md
