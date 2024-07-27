"""Test for Foo."""

from fastapi.testclient import TestClient

from api.main import health


def test_foo(my_object: dict[str, int]) -> None:
    """Test that my_object looks good."""
    assert my_object == {"first": 1, "second": 2}
    assert health() == "OK"


def test_health(client: TestClient) -> None:
    """Test the health of the API."""
    assert client.get("/health").json() == "OK"
