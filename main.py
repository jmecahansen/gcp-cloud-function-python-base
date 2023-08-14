"""
main application file
"""

# aliases and/or imports
from traceback import format_exc


def cloud_function(request):
    """
    Cloud Function entry point
    :param request: the request object
    :return: a Response object
    """

    try:
        # here goes your code
    except Exception as e:
        return f"{e}\n\n{format_exc()}", 500
