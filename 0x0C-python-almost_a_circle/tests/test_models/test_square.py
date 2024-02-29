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

    def test_str(self):
        s1 = Square(5)
        res = "[Square] (1) 0/0 - 5"
        s = Square.__str__(s1)
        self.assertEqual(s, res)
        
    def test_update_args(self):
        s1 = Square(10)
        s1.update(3)
        self.assertEqual(s1.id, 3)
        
        s1.update(4, 6)
        self.assertEqual(s1.size, 6)
        
        s1.update(4, 6, 39)
        self.assertEqual(s1.x, 39)
        
        s1.update(4, 6, 45, 100)
        self.assertEqual(s1.y, 100)
        
    def test_update_kwargs(self):
        s1 = Square(5)
        s1.update(**{ 'id': 89 })
        self.assertEqual(s1.id, 89)
        
        s1.update(**{ 'id': 89, 'size': 1 })
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        
        s1.update(**{ 'id': 89, 'size': 1, 'x': 2 })
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        
        s1.update(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        