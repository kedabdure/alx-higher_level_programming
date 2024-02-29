#!/usr/bin/python3
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

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

    def test_to_json(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        self.assertTrue(isinstance(dictionary, dict))
        json_dict = Base.to_json_string([dictionary])
        self.assertTrue(isinstance(json_dict, str))
        self.assertEqual('[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]', str(json_dict))

    def test_save_to_file(self):
        """Test save_to_file method."""
        r0 = Rectangle(10, 7, 2, 8)
        r1 = Rectangle(2, 4)
        Rectangle.save_to_file([r0, r1])
        res = ('[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},' +
               ' {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]')
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), len(res))

        os.remove("Rectangle.json")
        Rectangle.save_to_file([Rectangle(1, 2)])    
        res = ('[{"y": 0, "x": 0, "id": 1, "width": 1, "height": 2}]')
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), len(res))

    def test_save_none(self):
        Rectangle.save_to_file(None)
        res = "[]"
        with open("Rectangle.json", "r") as f:
            file = f.read()
        self.assertEqual(file, res)

    def test_save_empty(self):
        Rectangle.save_to_file([])
        res = "[]"
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), len(res))
            
    def test_save_sq_to_file(self):
        """Test save_to_file method."""
        r0 = Square(10, 7, 2, 8)
        r1 = Square(2, 4)
        Square.save_to_file([r0, r1])
        res = ('[{"id": 8, "size": 10, "x": 7, "y": 2}, {"id": 1, "size": 2, "x": 4, "y": 0}]')
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), len(res))
         
    def test_save_square1(self):   
        Square.save_to_file([Square(1, 2)])
        
        res = ('[{"y": 0, "x": 0, "id": 1, "size": 2}]')
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), len(res))
            print(f.read())
        
    def test_save_square(self):
        Square.save_to_file(None)
        res = "[]"
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), res)

    def test_sq_none(self):
        Square.save_to_file([])
        res = "[]"
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), res)

    def test_load_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_input = [r1, r2]
        Rectangle.save_to_file(list_input)
        list_output = Rectangle.load_from_file()
        self.assertEqual(len(list_input), len(list_output))
    