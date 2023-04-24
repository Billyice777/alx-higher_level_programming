#!/usr/bin/python3
"""Defining a Student Class"""


class Student:
    """
    Represents a student with first_name, last_name and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance with the given first_name, last_name, and age.
ii        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        Args:
            attrs (list): The list of attributes to retrieve. Defaults to None.
        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
