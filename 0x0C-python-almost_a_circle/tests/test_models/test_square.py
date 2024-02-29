#!/usr/bin/python3
"""Unittest for class Square"""

import unittest
import io
import contextlib
from models.base import Base
from models.square import Square

class TestSquare(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0
        
    def test_square_id(self):
        """Checking for id."""
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 5)

