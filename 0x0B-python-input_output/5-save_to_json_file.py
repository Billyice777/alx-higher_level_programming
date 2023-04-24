#!/usr/bin/python3
"""Defines a function that writes an Object to a textfile using JSON repr"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.
    Args:
        my_obj: The object to be written to the file.
        filename: The name of the file to write the JSON representation to.
    Returns:
        None
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
