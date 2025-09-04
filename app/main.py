from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes import web, api

app = FastAPI(title="Images AI")

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Routers
app.include_router(web.router)
app.include_router(api.router, prefix="/api")
