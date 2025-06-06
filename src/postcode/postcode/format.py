from enum import Enum


class PostcodeFormat(str, Enum):
    """Enumeration of supported postcode formats."""

    UK = "UK"
