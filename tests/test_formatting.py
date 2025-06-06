import pytest
from src.postcode.service import Service
from src.postcode.postcode.model import Postcode

from .data.formatting import (
    standard_formatting_cases,
    crown_formatting_cases,
    bfpo_formatting_cases,
    bot_formatting_cases,
    non_geographic_formatting_cases,
    special_formatting_cases,
)


@pytest.fixture(scope="module")
def postcode_service():
    """Shared postcode service using regex-based handler."""
    return Service.using_regex()


@pytest.mark.parametrize("postcode_input, expected", standard_formatting_cases)
def test_standard_postcode_formatting(postcode_input, expected, postcode_service):
    _assert_format(postcode_service, postcode_input, expected)


@pytest.mark.parametrize("postcode_input, expected", crown_formatting_cases)
def test_crown_dependency_postcode_formatting(
    postcode_input, expected, postcode_service
):
    _assert_format(postcode_service, postcode_input, expected)


@pytest.mark.parametrize("postcode_input, expected", bfpo_formatting_cases)
def test_bfpo_postcode_formatting(postcode_input, expected, postcode_service):
    _assert_format(postcode_service, postcode_input, expected)


@pytest.mark.parametrize("postcode_input, expected", bot_formatting_cases)
def test_bot_postcode_formatting(postcode_input, expected, postcode_service):
    _assert_format(postcode_service, postcode_input, expected)


@pytest.mark.parametrize("postcode_input, expected", non_geographic_formatting_cases)
def test_non_geographic_postcode_formatting(postcode_input, expected, postcode_service):
    _assert_format(postcode_service, postcode_input, expected)


@pytest.mark.parametrize("postcode_input, expected", special_formatting_cases)
def test_special_postcode_formatting(postcode_input, expected, postcode_service):
    _assert_format(postcode_service, postcode_input, expected)


def _assert_format(service, postcode_input, expected):
    result = service.parse_one(postcode_input)
    assert result.valid, f"{postcode_input} failed: {result.error}"
    postcode: Postcode = result.value
    assert postcode.area == expected["area"]
    assert postcode.district == expected["district"]
    assert postcode.sector == expected["sector"]
    assert postcode.unit == expected["unit"]
    assert postcode.outcode == expected["outcode"]
    assert postcode.incode == expected["incode"]
    assert postcode.full == expected["full"]
