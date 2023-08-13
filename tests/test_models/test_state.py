#!/usr/bin/python3
""" test for State """
import unittest
import pep8
from models.state import State

class State_testing(unittest.TestCase):
    """ check BaseModel class"""

    def testpep8(self):
        """ testing code style """
        pepstylecode = pep8.StyleGuide(quiet=True)
        user_path = 'models/state.py'
        result = pepstylecode.check_files([user_path])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
