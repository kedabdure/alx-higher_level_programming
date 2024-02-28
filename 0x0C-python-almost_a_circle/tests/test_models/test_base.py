#!/usr/bin/python3
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

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
        b9 = Base()
        self.assertEqual(type(b9), Base)
        
    # def test_save_to_file(self):
    #     """save to file"""
    #     r1 = Rectangle(4, 5)
    #     r2 = Rectangle(5, 6, 3)
        
    #     obj_list = ([r1, r2])
        
    #     Rectangle.save_to_file(obj_list)
    #     self.assertTrue(os.path.exists("Rectangle.json"))
        
    #     res = '[{"id": 6, "width": 4, "height": 5, "x": 0, "y": 0}, {"id": 7, "width": 5, "height": 6, "x": 3, "y": 0}]'
        
    #     with open("Rectangle.json", "r") as f:
    #         file = f.read()
    #     self.assertEqual(len(file), len(res))
    #     self.assertEqual(file, res)
        
    def test_save_none(self):
        r1 = Rectangle(4, 5)
        Rectangle.save_to_file(None)
        res = "[]"
        with open("Rectangle.json", "r") as f:
            file = f.read()
        self.assertEqual(file, res)
        
    def test_save_empty(self):
        r1 = Rectangle(4, 5)
        Rectangle.save_to_file([])
        res = "[]"
        with open("Rectangle.json", "r") as f:
            file = f.read()
        self.assertEqual(file, res)