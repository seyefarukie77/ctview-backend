# -----------------------------
# GLOBAL SETTINGS
# -----------------------------
PYTHON=python
BACKEND_DIR=backend
FRONTEND_DIR=frontend

# -----------------------------
# BACKEND COMMANDS
# -----------------------------
run-backend:
    cd $(BACKEND_DIR) && uvicorn app.main:app --reload

install-backend:
    cd $(BACKEND_DIR) && pip install -r requirements.txt

migrate:
    cd $(BACKEND_DIR) && alembic revision --autogenerate -m "auto migration"

upgrade:
    cd $(BACKEND_DIR) && alembic upgrade head

seed:
    cd $(BACKEND_DIR) && $(PYTHON) -m scripts.seed

# -----------------------------
# FRONTEND COMMANDS
# -----------------------------
install-frontend:
    cd $(FRONTEND_DIR) && npm install

run-frontend:
    cd $(FRONTEND_DIR) && npm run dev

build-frontend:
    cd $(FRONTEND_DIR) && npm run build

# -----------------------------
# FULL STACK COMMANDS
# -----------------------------
run:
    make run-backend & make run-frontend

install:
    make install-backend && make install-frontend

# -----------------------------
# AWS EB DEPLOYMENT
# -----------------------------
deploy:
    eb deploy

logs:
    eb logs

ssh:
    eb ssh

# -----------------------------
# CLEANUP
# -----------------------------
clean:
    find . -type d -name "__pycache__" -exec rm -r {} +
