#!/usr/bin/python3
""" User Class """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class that inherits from BaseModel Class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

