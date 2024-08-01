"""Where the API comes to life."""

from random import random

from fastapi import FastAPI

app = FastAPI()
DATA_LEN = 10


@app.get("/health")
def health() -> str:
    """Healthcheck."""
    return "OK"


@app.get("/data")
def data() -> list[float]:
    """Return some random data."""
    return [random() for _ in range(DATA_LEN)]
