"""
main application file
"""

# aliases and/or imports
from flask import Request, Response
from src.application import ApplicationClass
from traceback import format_exc


def cloud_function(request: Request) -> Response or tuple[str, int]:
    """
    Cloud Function entry point
    :param request: the request object
    :return: a Response object or a tuple with the response contents (text content and status code)
    """

    try:
        return ApplicationClass(request).run()
    except Exception as e:
        return f"{e}\n\n{format_exc()}", 500
