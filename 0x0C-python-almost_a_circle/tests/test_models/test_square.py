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
        
        s2 = Square(5, 6)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s2.size, 5)
        
        s3 = Square(5, 6, 4)
        self.assertEqual(s3.id, 3)
        self.assertEqual(s3.size, 5)
        self.assertEqual(s3.x, 6)
        
        s4 = Square(5, 6, 4, 8)
        self.assertEqual(s4.id, 8)
        self.assertEqual(s4.size, 5)
        self.assertEqual(s4.x,6)
        self.assertEqual(s4.y, 4)
        
    def test_validaton(self):
        with self.assertRaises(TypeError) as e:
            Square("1")
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            Square(3, "1")
        self.assertEqual("x must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            Square(3, 4, "1")
        self.assertEqual("y must be an integer", str(e.exception))

        with self.assertRaises(ValueError) as e:
            Square(-1)
        self.assertEqual("width must be > 0", str(e.exception))

        with self.assertRaises(ValueError) as e:
            Square(1, -1)
        self.assertEqual("x must be >= 0", str(e.exception))

        with self.assertRaises(ValueError) as e:
            Square(2, 1, -1)
        self.assertEqual("y must be >= 0", str(e.exception))

        with self.assertRaises(ValueError) as e:
            Square(0)
        self.assertEqual("width must be > 0", str(e.exception))
