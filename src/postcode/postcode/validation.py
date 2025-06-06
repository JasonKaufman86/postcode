import re

from .errors import (
    PostcodeFormatError,
    PostcodeLengthError,
    PostcodeTypeError,
)
from .normalize import strip_postcode
from ..error import log_and_raise


MIN_POSTCODE_LENGTH = 4
MAX_POSTCODE_LENGTH = 9
VALID_POSTCODE_CHARS = re.compile(r"^[A-Z0-9 \-]+$", re.IGNORECASE)


def validate_postcode_type(postcode: object) -> None:
    """Validate that the postcode is a string."""
    if not isinstance(postcode, str):
        log_and_raise(PostcodeTypeError(postcode=str(postcode)))


def validate_postcode_not_empty(postcode: str) -> None:
    """Validate that the postcode is not an empty string."""
    if strip_postcode(postcode) == "":
        log_and_raise(
            PostcodeFormatError(
                postcode=postcode,
                message=f"Postcode '{postcode}' cannot be empty or whitespace.",
            )
        )


def validate_postcode_chars(postcode: str) -> None:
    """Validate that the postcode contains only allowed characters."""
    if not VALID_POSTCODE_CHARS.match(postcode):
        log_and_raise(
            PostcodeFormatError(
                postcode=postcode,
                message=(f"Postcode '{postcode}' contains invalid characters. " "Only A-Z, 0-9, space, and hyphen are allowed."),
            )
        )


def validate_postcode_length(postcode: str) -> None:
    """Validate the length of the postcode."""
    stripped = strip_postcode(postcode)
    if not (MIN_POSTCODE_LENGTH <= len(stripped) <= MAX_POSTCODE_LENGTH):
        log_and_raise(
            PostcodeLengthError(
                postcode=postcode,
                min_length=MIN_POSTCODE_LENGTH,
                max_length=MAX_POSTCODE_LENGTH,
            )
        )


def validate_postcode(postcode: str) -> None:
    """Validate the postcode by checking type, content, length, and characters."""
    validate_postcode_type(postcode)
    validate_postcode_not_empty(postcode)
    validate_postcode_length(postcode)
    validate_postcode_chars(postcode)
