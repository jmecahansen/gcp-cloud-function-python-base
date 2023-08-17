"""
application (for testing purposes)
"""

# aliases and/or imports
from flask import Flask, request
from src.application import ApplicationClass
from traceback import format_exc

# initialize the app
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def cloud_function():
    """
    Cloud Function entry point
    :return: a Response object
    """

    try:
        return ApplicationClass(request).run()
    except Exception as e:
        return f"{e}\n\n{format_exc()}", 500
