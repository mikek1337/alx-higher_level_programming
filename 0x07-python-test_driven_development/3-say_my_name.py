#!/usr/bin/python3

"Module say_my_name"

def say_my_name(first_name, last_name=""):
    """
    Prints the first name and last name 
    """
    
    if not isinstance(first_name, str):
        TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))