"""Fixtures and such."""

from typing import Iterator

import pytest
from fastapi.testclient import TestClient

from api.main import app


@pytest.fixture(autouse=True, scope="function")
def my_object() -> Iterator[dict[str, int]]:
    """Some object to be reused in each test."""
    try:
        yield {"first": 1, "second": 2}
    finally:
        # cleanup
        pass


@pytest.fixture(scope="function")
def client() -> Iterator[TestClient]:
    """Test Client."""
    yield TestClient(app)
