#!/usr/bin/python3
""" test for Place"""
import unittest
import pep8
from models.place import Place

class Place_testing(unittest.TestCase):
    """ check the BaseModel class """

    def testpep8(self):
        """ testing the code style """
        pepstylecode = pep8.StyleGuide(quiet=True)
        user_path = 'models/place.py'
        result = pepstylecode.check_files([user_path])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
