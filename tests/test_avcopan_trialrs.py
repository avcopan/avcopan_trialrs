"""avcopan_trialrs tests."""

import avcopan_trialrs


def test_stub() -> None:
    """Stub test to ensure the test suite runs."""
    print(avcopan_trialrs.__version__)  # noqa: T201


def test__greet() -> None:
    """Test the greet function."""
    assert avcopan_trialrs.greet("World") == "Hello, World!"
