import pytest
from src.postcode.postcode.normalize import (
    strip_postcode,
    uppercase_postcode,
    normalize_postcode,
)


@pytest.mark.parametrize(
    "input_value, expected",
    [
        ("  SW1A 1AA ", "SW1A 1AA"),
        ("\nPO16 7GZ\t", "PO16 7GZ"),
        ("   ", ""),
        ("\n\t", ""),
    ],
)
def test_strip_postcode(input_value, expected):
    assert strip_postcode(input_value) == expected


@pytest.mark.parametrize(
    "input_value, expected",
    [
        ("sw1a 1aa", "SW1A 1AA"),
        ("Po16 7gz", "PO16 7GZ"),
        ("GU16 7hf", "GU16 7HF"),
    ],
)
def test_uppercase_postcode(input_value, expected):
    assert uppercase_postcode(input_value) == expected


@pytest.mark.parametrize(
    "input_value, expected",
    [
        ("  sw1a 1aa ", "SW1A 1AA"),
        ("\tpo16 7gz\n", "PO16 7GZ"),
        ("  gu16 7hf ", "GU16 7HF"),
        ("\n\nl1 8jq\t", "L1 8JQ"),
    ],
)
def test_normalize_postcode(input_value, expected):
    assert normalize_postcode(input_value) == expected
