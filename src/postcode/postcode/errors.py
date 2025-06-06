from enum import Enum

from ..error import Error


class PostcodeErrorCode(Enum):
    """Enumeration of error codes for postcode validation."""

    POSTCODE_ERROR = "POSTCODE_ERROR"
    POSTCODE_TYPE_ERROR = "POSTCODE_TYPE_ERROR"
    POSTCODE_FORMAT_ERROR = "POSTCODE_FORMAT_ERROR"
    POSTCODE_LENGTH_ERROR = "POSTCODE_LENGTH_ERROR"
    POSTCODE_NOT_FOUND_ERROR = "POSTCODE_NOT_FOUND_ERROR"


class PostcodeError(Error):
    """Base class for errors related to postcode validation."""

    def __init__(
        self,
        postcode: str,
        message: str = "Postcode error.",
        code: str = PostcodeErrorCode.POSTCODE_ERROR.value,
    ) -> None:
        self.postcode = postcode
        super().__init__(code, message)

    def __str__(self):
        return f"[{self.code}] [{self.postcode}] {self.message}"


class PostcodeTypeError(PostcodeError):
    """Error for invalid postcode type."""

    def __init__(self, postcode: str) -> None:
        super().__init__(
            postcode,
            f"Postcode '{postcode}' must be a string.",
            PostcodeErrorCode.POSTCODE_TYPE_ERROR.value,
        )


class PostcodeFormatError(PostcodeError):
    """Error for invalid postcode format."""

    def __init__(self, postcode: str, message: str = None) -> None:
        message = message or f"Postcode '{postcode}' has an invalid format."
        super().__init__(
            postcode,
            message,
            PostcodeErrorCode.POSTCODE_FORMAT_ERROR.value,
        )


class PostcodeLengthError(PostcodeError):
    """Error for invalid postcode length."""

    def __init__(self, postcode: str, min_length: int, max_length: int) -> None:
        super().__init__(
            postcode,
            f"Postcode '{postcode}' must be between {min_length} and {max_length} characters long.",
            PostcodeErrorCode.POSTCODE_LENGTH_ERROR.value,
        )


class PostcodeNotFoundError(PostcodeError):
    """Error for postcode not found."""

    def __init__(self, postcode: str) -> None:
        super().__init__(
            postcode,
            f"Postcode '{postcode}' not found.",
            PostcodeErrorCode.POSTCODE_NOT_FOUND_ERROR.value,
        )
