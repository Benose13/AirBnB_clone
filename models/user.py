#!/usr/bin/python3
"""
User module from BaseModel class
and contain all users info.
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    Initialze User class

    Attributes:
    email: empty string
    password: empty string
    first_name: empty string
    last_name: empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
