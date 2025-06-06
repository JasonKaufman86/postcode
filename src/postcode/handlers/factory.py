from .base import BaseHandler, BaseHandlerSettings
from .http.osdatahub import OSDataHubHttpHandler
from .http.postcode_io import PostcodeIOHttpHandler
from .regex import RegexHandler
from .types import HandlerType
from .errors import HandlerNotFoundError
from ..error import log_and_raise


class HandlerFactory:
    """Factory class to create handlers based on the handler type."""

    HANDLERS: dict[HandlerType, type[BaseHandler]] = {
        HandlerType.REGEX: RegexHandler,
        HandlerType.HTTP_POSTCODES_IO: PostcodeIOHttpHandler,
        HandlerType.HTTP_OSDATAHUB: OSDataHubHttpHandler,
    }

    @staticmethod
    def create(settings: BaseHandlerSettings) -> BaseHandler:
        """Create a handler based on the provided settings."""
        constructor = HandlerFactory.HANDLERS.get(settings.type)
        if not constructor:
            log_and_raise(HandlerNotFoundError(settings.type))
        return constructor(settings)
