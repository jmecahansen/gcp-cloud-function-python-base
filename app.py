"""
application (for testing purposes)
"""

# aliases and/or imports
from flask import Flask, request, Response
from src.application import ApplicationClass
from traceback import format_exc

# initialize the app
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def cloud_function() -> Response or tuple[str, int]:
    """
    Cloud Function entry point
    :return: a Response object or a tuple with the response contents (text content and HTTP response code)
    """

    try:
        return ApplicationClass(request).run()
    except Exception as e:
        return f"{e}\n\n{format_exc()}", 500
