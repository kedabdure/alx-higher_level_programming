#!/usr/bin/python3
import os
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    base = Base()
    def test_default_value(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 3)
        self.assertEqual(b3.id, 4)

    def test_custom_value(self):
        b1 = Base(4)
        b2 = Base(6)
        b3 = Base(20)
        self.assertEqual(b1.id, 4)
        self.assertEqual(b2.id, 6)
        self.assertEqual(b3.id, 20)
    
    def test_multiple_args_value(self):
        b1 = Base(4, 6)
        b2 = Base(6, 8)
        b3 = Base(5, 7)
        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 3)
        self.assertEqual(b3.id, 4)
