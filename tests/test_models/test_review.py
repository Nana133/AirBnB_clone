#!/usr/bin/python3
""" test for Review class """
import unittest
import pep8
from models.review import Review

class Review_testing(unittest.TestCase):
    """ check the BaseModel class"""

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        user_path = 'models/review.py'
        result = pepstylecode.check_files([user_path])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
