#!/usr/bin/python3
""" Unittest for the BaseModel class """
import unittest
import datetime
import uuid
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Tests the BaseModel class's methods and attributes. """

    def setUp(self):
        """ setup the kwargs properly """
        try:
            os.remove("file.json")
        except:
            pass
        self.base1 = BaseModel(number=89,
                               created_at="2020-06-28T01:25:18.335269",
                               updated_at="2020-06-28T01:25:18.335279",
                               id="0e6ad280-ebf5-4bc8-0671-2a0e8daff35d")
        self.base2 = BaseModel()
        self.base3 = BaseModel()

    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass

if __name__ == "__main__":
    unittest.main()
