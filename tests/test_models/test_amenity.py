#!/usr/bin/python3
""" testing Amenity class """
import unittest
import pep8
from models.amenity import Amenity

class Amenity_testing(unittest.TestCase):
    """ checking BaseModel class """

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        user_path = 'models/amenity.py'
        result = pepstylecode.check_files([user_path])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
