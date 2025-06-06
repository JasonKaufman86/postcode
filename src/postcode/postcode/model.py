from typing import Optional

from pydantic import BaseModel, Field

from .format import PostcodeFormat


class Postcode(BaseModel):
    """A model representing a postcode."""

    format: PostcodeFormat = Field(
        ...,
        description="The format of the postcode, e.g., 'UK'",
    )
    area: Optional[str] = Field(
        None,
        description="The area of the postcode, e.g., 'SW'.",
    )
    district: Optional[str] = Field(
        None,
        description="The district part of the outward code, e.g., '1A'.",
    )
    sector: Optional[str] = Field(
        None,
        description="The sector part of the inward code, e.g., '1'.",
    )
    unit: Optional[str] = Field(
        None,
        description="The unit of the postcode, e.g., 'AA'.",
    )

    @property
    def full(self) -> str:
        """Return the full postcode (outward + inward)."""
        return f"{self.outcode} {self.incode}"

    @property
    def outcode(self) -> str:
        """Return the outward code (area + district)."""
        return f"{self.area or ''}{self.district or ''}"

    @property
    def incode(self) -> str:
        """Return the inward code (sector + unit)."""
        return f"{self.sector or ''}{self.unit or ''}"

    def __str__(self):
        return (
            f"Postcode(format={self.format}, area={self.area}, "
            f"district={self.district}, sector={self.sector}, unit={self.unit}, "
            f"full={self.full}, outcode={self.outcode}, incode={self.incode})"
        )
