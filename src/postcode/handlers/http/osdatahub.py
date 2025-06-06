import requests
from pydantic import Field

from ..base import BaseHandler, BaseHandlerSettings
from ..regex import RegexHandler
from ..types import HandlerType
from ..errors import (
    HandlerTimeoutError,
    HandlerConnectionError,
    HandlerAPIError,
    HandlerNoResultsError,
)
from ...postcode.model import Postcode


class OSDataHubHandlerSettings(BaseHandlerSettings):
    """Settings for the OS Data Hub API handler."""

    type: str = Field(
        default=HandlerType.HTTP_OSDATAHUB.value,
        description="Type of the handler, used for identification.",
        init=False,
    )

    api_key: str = Field(..., description="API key for the OS Data Hub")
    timeout: float = Field(
        default=0.5,
        description="Timeout for API requests in seconds",
    )


class OSDataHubHttpHandler(BaseHandler):
    """Handler for parsing UK postcodes using the OS Data Hub API."""

    def __init__(self, settings: OSDataHubHandlerSettings):
        super().__init__()
        self._settings = settings
        self._endpoint = "https://api.os.uk/search/names/v1/find"

    @property
    def timeout(self) -> float:
        """Return the timeout setting for the API requests."""
        return self._settings.timeout

    def _handle(self, postcode: str) -> Postcode:
        """Handle the postcode string and return a Postcode object."""

        try:
            response = requests.get(
                self._endpoint,
                params={
                    "key": self._settings.api_key,
                    "query": postcode,
                    "maxresults": 1,
                },
                timeout=self.timeout,
            )

        except requests.Timeout:
            raise HandlerTimeoutError(self.__class__.__name__, self.timeout)

        except requests.ConnectionError:
            raise HandlerConnectionError(self.__class__.__name__)

        if response.status_code == 401:
            raise HandlerAPIError(
                self.__class__.__name__,
                response.status_code,
                "Invalid API key provided for OS Data Hub.",
            )

        if response.status_code != 200:
            raise HandlerAPIError(self.__class__.__name__, response.status_code)

        data = response.json()
        if not data.get("results"):
            raise HandlerNoResultsError(self.__class__.__name__, postcode)

        postcode_data = data["results"][0]["GAZETTEER_ENTRY"]["NAME1"]
        return RegexHandler.default().handle(postcode_data)
