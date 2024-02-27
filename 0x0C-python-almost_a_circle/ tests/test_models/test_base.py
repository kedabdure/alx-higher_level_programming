#!/usr/bin/python3
import os
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def setUp(self):
        Base.__nb_objects = 0
    
    def test_default_value(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_value(self):
        b1 = Base(4)
        b2 = Base(6)
        b3 = Base(20)
        self.assertEqual(b1.id, 4)
        self.assertEqual(b2.id, 6)
        self.assertEqual(b3.id, 20)
