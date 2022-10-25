#!/usr/bin/python3

"""Module load json from file to program"""

import json


def load_from_json_file(filename):
    """Function to read json from file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
