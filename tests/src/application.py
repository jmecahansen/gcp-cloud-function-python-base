"""
application
"""

# aliases and/or imports
from flask import Request, Response
from src.application import ApplicationClass
import pytest


@pytest.mark.parametrize("arguments, expectation ", [
    ({}, b"{\"status\":\"OK\"}"),
])
def test_response_matches_expectation(arguments: dict,
                                      expectation: str):
    """
    test the response matches its expectation
    :param arguments: the HTTP request arguments
    :param expectation: the expected JSON-encoded output
    """

    response = ApplicationClass(Request(arguments)).run()
    assert (
        isinstance(response, Response)
        and response.data == expectation
    )
