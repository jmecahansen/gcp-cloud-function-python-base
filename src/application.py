"""
application
"""

# aliases and/or imports
from flask import Request, Response
from src.helpers.request import build_response, get_data


class ApplicationClass:
    """
    application class
    """

    def __init__(self,
                 request: Request):
        """
        constructor
        :param request: the request object
        """

        self.request = request

    def run(self) -> Response:
        """
        run the application
        :return: a Response object
        """

        if not self.request:
            return build_response(400, "no request data")

        # here goes your code

        return build_response(200)
