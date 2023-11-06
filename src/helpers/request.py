"""
request
"""

# aliases and/or imports
from flask import Request, Response
from json import dumps
from src.defaults import json_encoding_options
from typing import Any


def build_response(code: int,
                   message: str = None,
                   data: dict or list = None) -> Response:
    """
    builds a response object
    :param code: the status code
    :param message: the text message (optional)
    :param data: the attached data (optional)
    :return: the response object
    """

    response = Response()
    response.data = dumps({key: value for key, value in {
        "data": data,
        "message": message,
        "status": "OK" if code in list(range(200, 299)) else "ERROR"
    }.items() if value}, **json_encoding_options)
    response.mimetype = "application/json"
    response.status_code = code
    return response


def get_data(request: Request,
             key: str,
             fallback: Any = None) -> Any:
    """
    return the value of a specific variable
    :param request: the request object
    :param key: the variable key
    :param fallback: the fallback value (optional)
    :return: the value
    """

    if not request:
        raise Exception("no request data")

    if (
        request.args
        and key in request.args
    ):
        return request.args.get(key)

    if (
        request.form
        and key in request.form
    ):
        return request.form.get(key)

    if request.json:
        data = request.get_json(silent=True)

        if key in data:
            return data[key]

    return fallback
