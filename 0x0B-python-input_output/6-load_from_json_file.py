#!/usr/bin/python3
"""Defines a function reads from a JSON file"""
import json


def load_from_json_file(filename):
    """Load an object from a file in JSON format."""
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
