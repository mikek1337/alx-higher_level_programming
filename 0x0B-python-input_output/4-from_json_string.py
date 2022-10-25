#!/usr/bin/python3

"""Module convert to string json to the object"""

import json


def from_json_string(my_str):
    """function converting string to json object"""
    return json.loads(my_str)
