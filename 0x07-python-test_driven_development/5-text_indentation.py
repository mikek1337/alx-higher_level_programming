#!/usr/bin/python3
"""
Module text indentation
"""


def text_indentation(text):
    """prints strings with new line if it has ., ?, :"""
    if not isinstance(text, str):
        raise TypeError("text must be string")
    res = []
    for i in text.split(" "):
        res.append(i+" ")
        if i.endswith(".") or i.endswith("?") or i.endswith(":"):
            res.append("\n")
    print("".join(res))
