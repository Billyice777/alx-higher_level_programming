#!/usr/bin/python3
"""Defines a function that converts JSON object to python object."""
import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.
    Args:
        my_str (str): A JSON string to be converted to an object.
    Returns:
        The Python object represented by the JSON string.
    """
    return json.loads(my_str)
