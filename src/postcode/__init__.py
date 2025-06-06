PACKAGE_NAME = "postcode"
PACKAGE_VERSION = "1.0.0"

from .postcode import (
    Postcode,
    PostcodeError,
    PostcodeErrorCode,
    PostcodeFormatError,
    PostcodeLengthError,
    PostcodeNotFoundError,
    PostcodeTypeError,
)
from .result import Result
from .error import Error, InternalError
from .logging import configure_logger
from .service import Service

__all__ = [
    "Postcode",
    "PostcodeError",
    "PostcodeErrorCode",
    "PostcodeFormatError",
    "PostcodeLengthError",
    "PostcodeNotFoundError",
    "PostcodeTypeError",
    "Result",
    "Error",
    "InternalError",
    "configure_logger",
    "Service",
]
