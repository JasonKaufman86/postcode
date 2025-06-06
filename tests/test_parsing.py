import pytest
from src.postcode.service import Service
from .data.parsing import (
    standard_postcodes,
    crown_dependency_postcodes,
    bot_postcodes,
    bfpo_postcodes,
    non_geographic_postcodes,
    special_postcodes,
    invalid_postcodes,
)


@pytest.fixture(scope="module")
def postcode_service():
    return Service.using_regex()


@pytest.mark.parametrize("postcode", standard_postcodes)
def test_standard_postcodes(postcode, postcode_service):
    result = postcode_service.parse_one(postcode)
    assert result.valid, f"Standard postcode failed: {postcode} -> {result.error}"


@pytest.mark.parametrize("postcode", crown_dependency_postcodes)
def test_crown_dependency_postcodes(postcode, postcode_service):
    result = postcode_service.parse_one(postcode)
    assert (
        result.valid
    ), f"Crown dependency postcode failed: {postcode} -> {result.error}"


@pytest.mark.parametrize("postcode", bot_postcodes)
def test_bot_postcodes(postcode, postcode_service):
    result = postcode_service.parse_one(postcode)
    assert result.valid, f"BOT postcode failed: {postcode} -> {result.error}"


@pytest.mark.parametrize("postcode", bfpo_postcodes)
def test_bfpo_postcodes(postcode, postcode_service):
    result = postcode_service.parse_one(postcode)
    assert result.valid, f"BFPO postcode failed: {postcode} -> {result.error}"


@pytest.mark.parametrize("postcode", non_geographic_postcodes)
def test_non_geographic_postcodes(postcode, postcode_service):
    result = postcode_service.parse_one(postcode)
    assert result.valid, f"Non-geographic postcode failed: {postcode} -> {result.error}"


@pytest.mark.parametrize("postcode", special_postcodes)
def test_special_postcodes(postcode, postcode_service):
    result = postcode_service.parse_one(postcode)
    assert result.valid, f"Special postcode failed: {postcode} -> {result.error}"


@pytest.mark.parametrize("postcode", invalid_postcodes)
def test_invalid_postcodes(postcode, postcode_service):
    result = postcode_service.parse_one(postcode)
    assert not result.valid, f"Expected failure for: {postcode} but got: {result.value}"
