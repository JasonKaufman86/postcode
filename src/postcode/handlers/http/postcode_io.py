import requests
from pydantic import Field

from ...postcode.model import Postcode
from ..base import BaseHandler, BaseHandlerSettings
from ..regex import RegexHandler
from ..types import HandlerType
from ..errors import (
    HandlerTimeoutError,
    HandlerConnectionError,
    HandlerAPIError,
    HandlerNoResultsError,
)


class PostcodeIOHandlerSettings(BaseHandlerSettings):
    """Settings for the Postcodes.io API handler."""

    type: str = Field(
        default=HandlerType.HTTP_POSTCODES_IO.value,
        description="Type of the handler, used for identification.",
        init=False,
    )

    timeout: float = Field(
        default=0.5,
        description="Timeout for API requests in seconds",
    )


class PostcodeIOHttpHandler(BaseHandler):
    """Handler for parsing UK postcodes using the Postcodes.io API."""

    def __init__(self, settings: PostcodeIOHandlerSettings):
        super().__init__()
        self._settings = settings
        self._endpoint = "https://api.postcodes.io/postcodes"

    @property
    def timeout(self) -> float:
        """Return the timeout setting for the API requests."""
        return self._settings.timeout

    def _handle(self, postcode: str) -> Postcode:
        """Handle the postcode string and return a Postcode object."""
        try:
            response = requests.get(
                f"{self._endpoint}/{postcode}",
                timeout=self.timeout,
            )

        except requests.Timeout:
            raise HandlerTimeoutError(self.__class__.__name__, self.timeout)

        except requests.ConnectionError:
            raise HandlerConnectionError(self.__class__.__name__)

        if response.status_code != 200:
            raise HandlerAPIError(self.__class__.__name__, response.status_code)

        data = response.json()
        if not data.get("result"):
            raise HandlerNoResultsError(self.__class__.__name__, postcode)

        result = data["result"]
        return RegexHandler.default().handle(result["postcode"])
