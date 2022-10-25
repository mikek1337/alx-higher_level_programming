#!/usr/bin/python3

"""Module to write json data to file"""

import json

def save_to_json_file(my_obj, filename):
    """Function to save json object to file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)