#!/usr/bin/python3

"""Test case module for rectangle"""

import unittest
from models.rectangle import Rectangle


class RectangleTestCase(unittest.TestCase):
    """Class rectangle test case"""

    def first_rectangle_testcase(self):
        """Test if rectangle inheritance"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def validate_attributes_testcase(self):
        pass


if __name__ == '__main__':
    unittest.main()
