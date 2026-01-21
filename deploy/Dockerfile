FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ /app

CMD ["python", "-c", "import app.core.config as c; print('CONFIG:', c.settings.SQLALCHEMY_DATABASE_URI)"]
