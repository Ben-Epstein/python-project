"""Where the API comes to life."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health() -> str:
    """Healthcheck."""
    return "OK"
