# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from base import change_to_base


def test_zero() -> None:
    """Check that we handle zero correctly."""
    assert change_to_base(0, 2) == '0'
    assert change_to_base(0, 10) == '0'
    assert change_to_base(0, 16) == '0'


def test_positive() -> None:
    """Check that we handle positive numbers correctly."""
    assert change_to_base(31, 2) == '11111'
    assert change_to_base(31, 5) == '111'
    assert change_to_base(31, 8) == '37'
    assert change_to_base(31, 10) == '31'
    assert change_to_base(31, 16) == '1F'


def test_negative() -> None:
    """Check that we handle negative numbers correctly."""
    assert change_to_base(-31, 2) == '-11111'
    assert change_to_base(-31, 5) == '-111'
    assert change_to_base(-31, 8) == '-37'
    assert change_to_base(-31, 10) == '-31'
    assert change_to_base(-31, 16) == '-1F'
