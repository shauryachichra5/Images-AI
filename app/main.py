import sys
from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Add parent dir to sys.path (for imports)
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.routes import web, api

app = FastAPI(title="Images AI")

# Absolute path to static folder
BASE_DIR = Path(__file__).resolve().parent  # points to "app"
STATIC_DIR = BASE_DIR / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Routers
app.include_router(web.router)
app.include_router(api.router, prefix="/api")
