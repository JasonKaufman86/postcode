from enum import Enum

from ..error import Error


class HandlerErrorCode(Enum):
    """Enumeration of error codes for handler execution."""

    HANDLER_ERROR = "HANDLER_ERROR"
    HANDLER_TIMEOUT_ERROR = "HANDLER_TIMEOUT_ERROR"
    HANDLER_NOT_FOUND_ERROR = "HANDLER_NOT_FOUND_ERROR"
    HANDLER_CONNECTION_ERROR = "HANDLER_CONNECTION_ERROR"
    HANDLER_API_ERROR = "HANDLER_API_ERROR"
    HANDLER_RESULTS_ERROR = "HANDLER_NO_RESULTS_ERROR"


class HandlerError(Error):
    """Base class for errors related to postcode handlers."""

    def __init__(
        self,
        handler: str,
        message: str = "Handler error.",
        code: str = HandlerErrorCode.HANDLER_ERROR.value,
    ) -> None:
        self.handler = handler
        super().__init__(code, message)

    def __str__(self):
        return f"[{self.code}] [{self.handler}] {self.message}"


class HandlerTimeoutError(HandlerError):
    """Error for handler request timeouts."""

    def __init__(self, handler: str, timeout: int) -> None:
        super().__init__(
            handler,
            f"{handler} timed out after {timeout} seconds.",
            HandlerErrorCode.HANDLER_TIMEOUT_ERROR.value,
        )


class HandlerNotFoundError(HandlerError):
    """Error for unknown or unsupported handler types."""

    def __init__(self, handler: str) -> None:
        super().__init__(
            handler=handler,
            message=f"No handler registered for type '{handler}'.",
            code=HandlerErrorCode.HANDLER_NOT_FOUND_ERROR.value,
        )


class HandlerConnectionError(HandlerError):
    """Raised when a handler fails to connect to its data source."""

    def __init__(self, handler: str):
        super().__init__(
            handler=handler,
            message=f"{handler} failed to connect. Please check your network or API endpoint.",
            code=HandlerErrorCode.HANDLER_CONNECTION_ERROR.value,
        )


class HandlerAPIError(HandlerError):
    """Raised when a handler API returns a bad HTTP status."""

    def __init__(self, handler: str, status_code: int, message: str = None):
        super().__init__(
            handler=handler,
            message=message or f"{handler} returned unexpected status code {status_code}.",
            code=HandlerErrorCode.HANDLER_API_ERROR.value,
        )


class HandlerNoResultsError(HandlerError):
    """Raised when a handler API returns no usable results."""

    def __init__(self, handler: str, query: str):
        super().__init__(
            handler=handler,
            message=f"{handler} returned no results for query '{query}'.",
            code=HandlerErrorCode.HANDLER_RESULTS_ERROR.value,
        )
