def strip_postcode(postcode: str) -> str:
    """Strip leading and trailing whitespace from a postcode string."""
    return postcode.strip()


def uppercase_postcode(postcode: str) -> str:
    """Convert a postcode string to uppercase."""
    return postcode.upper()


def normalize_postcode(postcode: str) -> str:
    """Normalize spacing and casing of a postcode string."""
    return uppercase_postcode(strip_postcode(postcode))
