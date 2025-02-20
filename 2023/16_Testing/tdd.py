import pytest

def fibonacci(n: int)->int:
    """Return the n-th Fibonacci number."""
    if not isinstance(n, int):
        return None
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)


@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    ('a', None),
    (None, None)
])
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected