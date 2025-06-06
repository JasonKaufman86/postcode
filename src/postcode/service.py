from .handlers.base import BaseHandler, BaseHandlerSettings
from .handlers.factory import HandlerFactory
from .handlers.regex import RegexHandlerSettings
from .handlers.http.postcode_io import PostcodeIOHandlerSettings
from .handlers.http.osdatahub import OSDataHubHandlerSettings
from .handlers.errors import HandlerError
from .postcode.normalize import normalize_postcode
from .postcode.validation import validate_postcode
from .postcode.errors import PostcodeError
from .result import Result
from .error import Error, InternalError
from .logging import logger


class Service:
    """
    Public API for validating and parsing UK postcodes.

    The `Service` class uses pluggable handler backends to validate, normalize,
    and extract postcode components like area, district, sector, and unit.

    Handlers can be swapped for offline (regex) or online (Postcode.io, OS Data Hub) lookups.

    Example:
        service = Service.using_regex()
        result = service.parse_one("SW1A 1AA")
        if result.valid:
            print(result.value.area)  # => 'SW'

    ### Core Methods
    - parse_one(postcode): Parse and validate a single postcode.
    - parse_many(postcodes): Bulk parse multiple postcodes.
    - validate_one(postcode): Check if a postcode is valid.
    - validate_many(postcodes): Bulk validation.

    ### Factory Methods
    - using_regex(): Use built-in regex validation (offline).
    - using_postcode_io(): Use Postcode.io API (online).
    - using_osdatahub(): Use OS Data Hub API (online).
    """

    def __init__(self, handler: BaseHandler):
        self._handler = handler

    # ------------------------------------------------------------------
    # Parsing Methods
    # ------------------------------------------------------------------

    def parse_one(self, postcode: str) -> Result:
        """
        Validate and parse a single postcode.

        This will normalize and validate the input, then return a `Result` containing either
        the parsed `Postcode` model or a structured `Error`.

        Args:
            postcode (str): The raw postcode string (can be lowercased, spaced, etc.).

        Returns:
            Result: Contains the parsed postcode or an error.
        """
        try:
            validate_postcode(postcode)
            return Result.success(self._handler.handle(normalize_postcode(postcode)))
        except (PostcodeError, HandlerError, InternalError, Error) as e:
            return Result.failure(e)
        except Exception as e:
            error = InternalError(f"An unexpected error occurred while parsing postcode '{postcode}': {str(e)}")
            logger.exception(str(error))
            return Result.failure(error)

    def parse_many(self, postcodes: list[str]) -> list[Result]:
        """
        Validate and parse a list of postcodes.

        Args:
            postcodes (list[str]): A list of postcode strings.

        Returns:
            list[Result]: A list of results, one for each postcode.
        """
        return [self.parse_one(p) for p in postcodes]

    # ------------------------------------------------------------------
    # Validation Methods
    # ------------------------------------------------------------------

    def validate_one(self, postcode: str) -> bool:
        """
        Validate a single postcode.

        This method only returns whether the postcode is structurally valid,
        not its parsed representation.

        Args:
            postcode (str): The postcode to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        return self.parse_one(postcode).valid

    def validate_many(self, postcodes: list[str]) -> list[bool]:
        """
        Validate multiple postcodes.

        Args:
            postcodes (list[str]): A list of postcode strings.

        Returns:
            list[bool]: List of booleans representing the validity of each postcode.
        """
        return [self.validate_one(p) for p in postcodes]

    # ------------------------------------------------------------------
    # Factory Methods
    # ------------------------------------------------------------------

    @classmethod
    def create(cls, settings: BaseHandlerSettings) -> "Service":
        """
        Create a Service instance using the provided handler settings.

        Args:
            settings (BaseHandlerSettings): Configuration for the handler.

        Returns:
            Service: A fully constructed service instance.
        """
        return cls(HandlerFactory.create(settings))

    @classmethod
    def using_regex(cls) -> "Service":
        """
        Create a Service using the built-in regex-based validation.

        This is the default handler and requires no network access.

        Returns:
            Service: Regex-backed postcode service.
        """
        return cls.create(RegexHandlerSettings())

    @classmethod
    def using_postcode_io(cls, timeout: float = 5) -> "Service":
        """
        Create a Service using the Postcode.io API handler.

        Args:
            timeout (float): Timeout for HTTP requests in seconds.

        Returns:
            Service: Postcode.io-backed postcode service.
        """
        return cls.create(PostcodeIOHandlerSettings(timeout=timeout))

    @classmethod
    def using_osdatahub(cls, api_key: str, timeout: float = 5) -> "Service":
        """
        Create a Service using the OS Data Hub API handler.

        Args:
            api_key (str): API key for OS Data Hub.
            timeout (float): Timeout for HTTP requests in seconds.

        Returns:
            Service: OS Data Hub-backed postcode service.
        """
        return cls.create(OSDataHubHandlerSettings(api_key=api_key, timeout=timeout))
