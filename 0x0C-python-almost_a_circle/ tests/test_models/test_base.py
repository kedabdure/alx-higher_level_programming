#!/usr/bin/python3
import os
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def setUp(self):
        Base.__nb_objects = 0
    
    def test_default_value(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(4)
        self.assertEqual(b4.id, 4)
        b5 = Base(-20)
        self.assertEqual(b5.id, -20)
        b7 = Base(600)
        self.assertEqual(b7.id, 600)

    def test_for_type(self):
        b8 = Base()
        self.assertEqual(type(b8), Base)
        b9 = Base(8)
        self.assertEqual(type(b9), Base)
