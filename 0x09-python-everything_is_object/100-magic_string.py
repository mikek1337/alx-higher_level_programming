#!/usr/bin/python
def magic_string():
    magic_string.iterate = getattr(magic_string, 'iterate') + 1
    return ("BestSchool"*( magic_string.iterate - 1) + ", BestSchool")