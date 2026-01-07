FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# TEMPORARY DEBUG LINE
CMD ["python", "-c", "import app.core.config as c; print('CONFIG:', c.settings.SQLALCHEMY_DATABASE_URI)"]