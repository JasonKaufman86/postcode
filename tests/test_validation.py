import pytest
from src.postcode.postcode.validation import (
    validate_postcode_type,
    validate_postcode_not_empty,
    validate_postcode_length,
    validate_postcode_chars,
    validate_postcode,
)
from src.postcode.postcode.errors import (
    PostcodeTypeError,
    PostcodeLengthError,
    PostcodeFormatError,
)

# ------------------------------------------------------------------------
# Type Validation
# ------------------------------------------------------------------------


@pytest.mark.parametrize("value", ["SW1A 1AA", "AB12-3CD"])
def test_validate_postcode_type_accepts_valid_strings(value):
    validate_postcode_type(value)


@pytest.mark.parametrize("value", [123, None, ["SW1A 1AA"], {"postcode": "EC1A 1BB"}])
def test_validate_postcode_type_raises_for_non_string(value):
    with pytest.raises(PostcodeTypeError):
        validate_postcode_type(value)


# ------------------------------------------------------------------------
# Empty or Whitespace Validation
# ------------------------------------------------------------------------


@pytest.mark.parametrize("value", ["", "   ", "\n", "\t"])
def test_validate_postcode_not_empty_raises_on_blank(value):
    with pytest.raises(PostcodeFormatError):
        validate_postcode_not_empty(value)


@pytest.mark.parametrize("value", ["SW1A 1AA", "W1A-0AX"])
def test_validate_postcode_not_empty_allows_valid(value):
    validate_postcode_not_empty(value)


# ------------------------------------------------------------------------
# Length Validation
# ------------------------------------------------------------------------


@pytest.mark.parametrize("value", ["A1", "Z9"])
def test_validate_postcode_length_too_short(value):
    with pytest.raises(PostcodeLengthError):
        validate_postcode_length(value)


@pytest.mark.parametrize("value", ["ABCDEFGHIJK", "AB12 3CD XYZ"])
def test_validate_postcode_length_too_long(value):
    with pytest.raises(PostcodeLengthError):
        validate_postcode_length(value)


@pytest.mark.parametrize("value", ["SW1A 1AA", "AB1 2CD", "EC1A-1BB"])
def test_validate_postcode_length_valid(value):
    validate_postcode_length(value)


# ------------------------------------------------------------------------
# Character Validation
# ------------------------------------------------------------------------


@pytest.mark.parametrize("value", ["SW1A/1AA", "EC1A_1BB", "ABC@123"])
def test_validate_postcode_chars_invalid(value):
    with pytest.raises(PostcodeFormatError):
        validate_postcode_chars(value)


@pytest.mark.parametrize("value", ["SW1A 1AA", "W1A-0AX", "EC1A-1BB"])
def test_validate_postcode_chars_valid(value):
    validate_postcode_chars(value)


# ------------------------------------------------------------------------
# Full Postcode Validation
# ------------------------------------------------------------------------


@pytest.mark.parametrize("value", ["SW1A 1AA", "W1A-0AX"])
def test_validate_postcode_valid(value):
    validate_postcode(value)


@pytest.mark.parametrize("value", ["", "  /", 123, "A/", "A1"])
def test_validate_postcode_invalid(value):
    with pytest.raises((PostcodeTypeError, PostcodeFormatError, PostcodeLengthError)):
        validate_postcode(value)
