from typing import Iterator
import pytest

@pytest.fixture(always=True, scope="function")
def my_object() -> Iterator[dict[str, int]]:
    try:
        yield {"first": 1, "second": 2}
    finally:
        # cleanup
        pass