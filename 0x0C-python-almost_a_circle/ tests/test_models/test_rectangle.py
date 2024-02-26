#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_default_value(self):
        r1 = Rectangle()

        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
