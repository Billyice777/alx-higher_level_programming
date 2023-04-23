#!/usr/bin/python3
""" Module containing the BaseGeometry class """

    BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Implements a rectangle"""

    def __init__(self, width, height):
        """Initializes an instance of class Rectangle"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
