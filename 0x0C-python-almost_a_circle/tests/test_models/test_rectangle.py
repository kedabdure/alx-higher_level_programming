#!/usr/bin/python3
"""Unittest for class rectangle"""

import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        Base._Base__nb_objects = 0
        
    def tearDown(self):
        pass

    def test_rec_id(self):
        """Checking for id."""
        r0 = Rectangle(1, 2)
        self.assertEqual(r0.id, 1)
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.id, 2)
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.id, 3)

    def test_default_value(self):
        """checking multiple arg""" 
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        r4 = Rectangle(10, 2, 4, 5, 34)
        self.assertEqual(r4.id, 34)

    def test_passing_id(self):
        """checking custom id"""
        r5 = Rectangle(10, 2, 4, 5, -5)
        self.assertEqual(r5.id, -5)
        r6 = Rectangle(10, 2, 4, 5, 9)
        self.assertEqual(r6.id, 9)

    def test_passing_string(self):
        """checking string as id"""
        with self.assertRaises(TypeError) as x:
            o1 = Rectangle("1", 2)
        self.assertEqual("width must be an integer", str(x.exception))
        
        with self.assertRaises(TypeError) as x:
            o2 = Rectangle(1, "2")
        self.assertEqual("height must be an integer", str(x.exception))
        
        with self.assertRaises(TypeError) as x:
            o3 = Rectangle(1, 2, "3")
        self.assertEqual("x must be an integer", str(x.exception))
        
        with self.assertRaises(TypeError) as x:
            o4 = Rectangle(1, 2, 3, "4")
        self.assertEqual("y must be an integer", str(x.exception))
        
        with self.assertRaises(ValueError) as x:
            o5 = Rectangle(0, 2)
        self.assertEqual("width must be > 0", str(x.exception))
        
        with self.assertRaises(ValueError) as x:
            o6 = Rectangle(8, 0)
        self.assertEqual("height must be > 0", str(x.exception))
        
        with self.assertRaises(ValueError) as x:
            o7 = Rectangle(8, 5, -6)
        self.assertEqual("x must be >= 0", str(x.exception))
        
        with self.assertRaises(ValueError) as x:
            o8 = Rectangle(8, 5, 6, -7)
        self.assertEqual("y must be >= 0", str(x.exception))

    def test_area(self):
        """check the area"""
        r7 = Rectangle(4, 6)
        self.assertEqual(r7.area(), 24)
        r8 = Rectangle(6, 7)
        self.assertEqual(r8.area(), 42)

    def test_display(self):
        """check for display"""
        f = io.StringIO()
        r9 = Rectangle(2, 3)

        with contextlib.redirect_stdout(f):
            r9.display()
        s = f.getvalue()
        res = "##\n##\n##\n"
        self.assertEqual(s, res)
