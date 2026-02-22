import os

from fastapi import FastAPI


app = FastAPI(title="Deployment Observability API", version="1.0.0")


@app.get("/")
def root():
    return {
        "service": "deployment-observability-api",
        "status": "ok",
        "port": int(os.getenv("APP_PORT", "7056")),
    }


@app.get("/health")
def health():
    return {"ok": True}


@app.get("/observability")
def observability():
    return {
        "ready": True,
        "checks": {
            "http": "pass",
            "container": "pass",
        },
    }
