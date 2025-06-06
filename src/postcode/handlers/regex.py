"""
Regex-based Postcode Handler.

This module defines a handler that validates and parses postcodes using regular expressions.
It supports standard UK formats, as well as special cases such as BFPO, Eircode, and postcodes
from British Overseas Territories (BOT).

The standard UK postcode patterns are based on the official specification:
- Web Services Interface Specification v6.4, page 77:
  https://assets.publishing.service.gov.uk/media/632b07338fa8f53cb77ef6b8/WS02_LRS_Web_Services_Interface_Specification_v6.4.pdf

Special postcode formats and exceptions (e.g., GIR 0AA, BOT codes, AI-2640, KY1-1001, etc.)
are informed by examples documented here:
- Wikipedia - Postcodes in the United Kingdom, Special cases:
  https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Special_cases
"""

import re
from typing import List, Optional

from pydantic import Field

from .base import BaseHandler, BaseHandlerSettings
from .types import HandlerType

from ..logging import logger
from ..postcode.errors import PostcodeNotFoundError
from ..postcode.model import Postcode, PostcodeFormat


class RegexRule:
    """A rule that matches one or more regex patterns for a given postcode type."""

    def __init__(
        self,
        type: PostcodeFormat,
        patterns: List[str],
    ):
        self.type = type
        self.patterns = [re.compile(p) for p in patterns]

    def match(self, value: str) -> Optional[Postcode]:
        """Match the value against the regex patterns and return a Postcode object if matched."""
        logger.debug("Matching value '%s' against patterns for type '%s'", value, self.type)
        for regex in self.patterns:
            match = regex.match(value)
            if match:
                logger.debug("Matched value '%s' with regex '%s'", value, regex.pattern)
                groups = match.groupdict()
                return Postcode(
                    format=self.type,
                    area=groups.get("area"),
                    district=groups.get("district"),
                    sector=groups.get("sector"),
                    unit=groups.get("unit"),
                )

        logger.debug("No match found for value '%s' with type '%s'", value, self.type)
        return None


class RegexHandlerSettings(BaseHandlerSettings):
    """Settings for the RegexHandler."""

    type: str = Field(
        default=HandlerType.REGEX.value,
        description="Type of the handler, used for identification.",
        init=False,
    )


class RegexHandler(BaseHandler):
    """Handler for postcodes using regular expressions."""

    RULES = [
        RegexRule(
            PostcodeFormat.UK,
            [
                # ---------------------------------------------------------------------
                # Standard cases (BS7666)
                # ---------------------------------------------------------------------
                # Standard UK postcode formats
                r"^(?P<area>(?:BF1|[A-Z]{1,2}))(?P<district>[0-9]{1,2}[A-Z]?) ?(?P<sector>[0-9])(?P<unit>[ABDEFGHJLNPQRSTUWXYZ]{2})$",
                # BFPO: formats like BFPO 1234
                r"^BFPO ?(?P<unit>[0-9]{1,4})$",
                # Eircode: formats like D02 ABC4 or D6W 1234
                r"^(?P<area>[AC-FHKNPRTV-Y]{1}[0-9]{1,2}|D6W) ?(?P<unit>[0-9AC-FHKNPRTV-Y]{4})$",
                # ---------------------------------------------------------------------
                # Special cases
                # ---------------------------------------------------------------------
                # British Overseas Territories (BOT) postcodes: ASCN 1ZZ etc.
                r"^(?P<area>[A-Z]{4}) ?(?P<sector>[0-9])(?P<unit>[A-Z]{2})$",
                # Anguilla: AI-2640
                r"^(?P<area>AI)-(?P<unit>[0-9]{4})$",
                # Cayman Islands: KY1-1001
                r"^(?P<area>KY[1-3])-(?P<unit>[0-9]{4})$",
                # Montserrat: MSR-1110
                r"^(?P<area>MSR)-(?P<unit>[0-9]{4})$",
                # British Virgin Islands: VG1110
                r"^(?P<area>VG)(?P<unit>[0-9]{4})$",
                # Bermuda: formats like HM 01 or HM BX
                r"^(?P<area>[A-Z]{2}) (?P<unit>[0-9]{2}|BX)$",
                # Special case for the GIR postcode
                r"^(?P<area>GIR) ?(?P<sector>0)(?P<unit>AA)$",
            ],
        )
    ]

    def __init__(self, settings: RegexHandlerSettings):
        self._settings = settings

    def _handle(self, postcode: str) -> Postcode:
        """Handle the postcode string and return a Postcode object."""
        for rule in self.RULES:
            parsed = rule.match(postcode)
            if parsed:
                return parsed
        raise PostcodeNotFoundError(postcode)

    @classmethod
    def default(cls) -> "RegexHandler":
        """Create a default RegexHandler."""
        return cls(RegexHandlerSettings())
