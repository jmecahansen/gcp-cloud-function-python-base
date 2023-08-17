"""
request
"""

# aliases and/or imports
from flask import Response
from json import dumps
from src.defaults import json_encoding_options


def build_response(code: int,
                   message: str = None,
                   data: dict or list = None) -> Response:
    """
    builds a response object
    :param code: the HTTP response code
    :param message: the response message (optional)
    :param data: the response data (optional)
    :return: the response object
    """

    response = Response()
    response.charset = "utf-8"
    response.data = dumps({key: value for key, value in {
        "data": data,
        "message": message,
        "status": "OK" if code in list(range(200, 299)) else "ERROR"
    }.items() if value}, **json_encoding_options)
    response.mimetype = "application/json"
    response.status_code = code
    return response
