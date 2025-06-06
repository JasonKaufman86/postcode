from enum import Enum


class HandlerType(str, Enum):
    """Enumeration of known handler types."""

    REGEX = "regex"
    HTTP_POSTCODES_IO = "http_postcodes_io"
    HTTP_OSDATAHUB = "http_osdatahub"
