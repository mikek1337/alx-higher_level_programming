#!/usr/bin/python3

"""Class module of Mylist"""


class MyList(list):
    """MyList class that inherits from list"""

    def print_sorted(self):
        """prints sorted list"""
        lists = list(self)
        print(sorted(lists))
