from typing import Optional
from pydantic import BaseModel, Field

from .error import Error
from .postcode.model import Postcode


class Result(BaseModel):
    """
    Represents the outcome of a postcode validation and formatting operation.

    This model encapsulates either a successfully validated and parsed postcode (`value`)
    or a structured error object (`error`) that describes what went wrong. It is used as
    the return type of the Service to convey both success and failure states in a
    consistent, predictable way.

    ### Examples:
    Successful result:
        Result(
            value=Postcode(format='UK', area='SW', district='1A', sector='1', unit='AA'),
            error=None
        )

    Failed result:
        Result(
            value=None,
            error=Error(code='POSTCODE_FORMAT_ERROR', message='Invalid postcode structure')
        )

    ### Attributes:
    - value: The validated and parsed `Postcode` object if successful, else `None`.
    - error: An `Error` object describing the failure reason, if any.
    """

    value: Optional[Postcode] = Field(None, description="The validated and parsed postcode, if validation succeeded.")
    error: Optional[Error] = Field(
        None,
        description="Structured error describing why postcode validation failed, if applicable.",
    )

    @property
    def valid(self) -> bool:
        """Return True if the postcode is valid and parsed successfully."""
        return self.value is not None

    @classmethod
    def success(cls, value: Postcode) -> "Result":
        """Construct a Result representing a successful postcode parsing."""
        return cls(value=value)

    @classmethod
    def failure(cls, error: Error) -> "Result":
        """Construct a Result representing a failed postcode validation."""
        return cls(error=error)

    model_config = {"arbitrary_types_allowed": True}
