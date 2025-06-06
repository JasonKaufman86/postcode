from .logging import logger


class Error(Exception):
    """A structured error with a code and message."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return f"[{self.code}] {self.message}"


class InternalError(Error):
    """A generic internal error for unexpected failures."""

    def __init__(self, message: str = "An internal error occurred.") -> None:
        super().__init__("INTERNAL_ERROR", message)
        logger.exception(message)


def log_and_raise(error: Error) -> None:
    """Log the exception and raise it."""
    logger.error(str(error), stacklevel=3)
    raise error
