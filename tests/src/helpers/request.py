"""
request
"""

# aliases and/or imports
from flask import Response
from src.helpers.request import build_response
import pytest


@pytest.mark.parametrize("code, expectation ", [
    (200, b"{\"status\":\"OK\"}"),
    (301, b"{\"status\":\"ERROR\"}"),
    (302, b"{\"status\":\"ERROR\"}"),
    (400, b"{\"status\":\"ERROR\"}"),
    (404, b"{\"status\":\"ERROR\"}"),
    (410, b"{\"status\":\"ERROR\"}"),
    (500, b"{\"status\":\"ERROR\"}"),
])
def test_response_without_message_or_payload_matches_expectation(code: int,
                                                                 expectation: str):
    """
    test the response (without message or payload) matches its expectation
    :param code: the HTTP response code
    :param expectation: the expected JSON-encoded output
    """

    response = build_response(code)
    assert (
        isinstance(response, Response)
        and response.data == expectation
    )


@pytest.mark.parametrize("code, message, expectation ", [
    (200, "OK", b"{\"message\":\"OK\",\"status\":\"OK\"}"),
    (400, "missing field: foo", b"{\"message\":\"missing field: foo\",\"status\":\"ERROR\"}"),
])
def test_response_without_payload_matches_expectation(code: int,
                                                      message: str,
                                                      expectation: str):
    """
    test the response (without payload) matches its expectation
    :param code: the HTTP response code
    :param message: the message included with the response
    :param expectation: the expected JSON-encoded output
    """

    response = build_response(code, message)
    assert (
        isinstance(response, Response)
        and response.data == expectation
    )


@pytest.mark.parametrize("code, message, payload, expectation ", [
    (200, "OK", [1, 2, 3, 4, 5], b"{\"data\":[1,2,3,4,5],\"message\":\"OK\",\"status\":\"OK\"}"),
    (200, "OK", {
        "foo": 1,
        "bar": "hello"
    }, b"{\"data\":{\"foo\":1,\"bar\":\"hello\"},\"message\":\"OK\",\"status\":\"OK\"}"),
    (400, "missing field: baz", [1, 2, 3, 4, 5], b"{\"data\":[1,2,3,4,5],\"message\":\"missing field: baz\",\"status\":"
                                                 b"\"ERROR\"}"),
    (400, "missing field: baz", {
        "foo": 1,
        "bar": "hello"
    }, b"{\"data\":{\"foo\":1,\"bar\":\"hello\"},\"message\":\"missing field: baz\",\"status\":\"ERROR\"}"),
])
def test_response_matches_expectation(code: int,
                                      message: str,
                                      payload: dict or list,
                                      expectation: str):
    """
    test the response matches its expectation
    :param code: the HTTP response code
    :param message: the message included with the response
    :param payload: the payload included with the response
    :param expectation: the expected JSON-encoded output
    """

    response = build_response(code, message, payload)
    assert (
        isinstance(response, Response)
        and response.data == expectation
    )
