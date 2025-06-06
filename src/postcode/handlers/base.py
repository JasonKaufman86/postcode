from abc import ABC, abstractmethod

from pydantic import BaseModel, Field

from .errors import HandlerError
from ..postcode.model import Postcode
from ..postcode.errors import PostcodeError
from ..error import log_and_raise, InternalError, Error


class BaseHandlerSettings(BaseModel):
    """Base class for handler settings."""

    type: str = Field(
        description="Type of the handler, used for identification.",
    )


class BaseHandler(ABC):
    """Base class for postcode handlers."""

    def handle(self, postcode: str) -> Postcode:
        """Handle a postcode string and return a Postcode."""
        try:
            return self._handle(postcode)

        except (PostcodeError, HandlerError, Error) as e:
            log_and_raise(e)

        except Exception as e:
            log_and_raise(
                InternalError(
                    f"An unexpected error occurred while handling postcode '{postcode}': {str(e)}",
                ),
            )

    @abstractmethod
    def _handle(self, postcode: str) -> Postcode:
        """Handle a postcode string and return a Postcode."""
