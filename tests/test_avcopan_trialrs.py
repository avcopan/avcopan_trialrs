"""avcopan_trialrs tests."""

import pytest

import avcopan_trialrs


def test_stub() -> None:
    """Stub test to ensure the test suite runs."""
    print(avcopan_trialrs.__version__)  # noqa: T201


def test__greet() -> None:
    """Test the greet function."""
    assert avcopan_trialrs.greet("World") == "Hello, World!"


def test__greet__empty_name() -> None:
    """Test that greet raises an error for an empty name."""
    with pytest.raises(avcopan_trialrs.EmptyNameError, match="the name is empty"):
        avcopan_trialrs.greet("")
    assert issubclass(avcopan_trialrs.EmptyNameError, avcopan_trialrs.Error)
