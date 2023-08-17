"""
application defaults
"""

# aliases and/or imports
from os.path import abspath, dirname, relpath

# JSON encoding options
json_encoding_options = {
    "ensure_ascii": False,
    "separators": (":", ",")
}

# root application path
root_path = abspath(relpath(f"{dirname(__file__)}/.."))
