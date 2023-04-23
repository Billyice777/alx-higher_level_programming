#!/usr/bin/python3
"""
Module for is_same_class
"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a specified class"""
    return type(obj) is a_class
