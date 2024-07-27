"""Test for Foo."""

from api.main import health


def test_foo(my_object: dict[str, int]) -> None:
    """Test that my_object looks good."""
    assert my_object == {"first": 1, "second": 2}
    assert health() == "OK"
