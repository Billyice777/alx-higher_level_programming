#!/usr/bin/python3
"""A class to represent a List Object"""


class MyList(list):
    """This is a class that inherits from the list class"""

    def print_sorted(self):
        """This is a method that prints the sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
