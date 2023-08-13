#!/usr/bin/python3
""" test for User """
import unittest
import pep8
from models.user import User

class User_testing(unittest.TestCase):
    """ check BaseModel class """

    def testpep8(self):
        """ test for codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        user_path = 'models/user.py'
        result = pepstylecode.check_files([user_path])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
