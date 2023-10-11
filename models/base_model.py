#!/usr/bin/python3
"""Defines the BaseModel class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel as the base for other classes."""
    def __init__(self):
        """Instance attributes for BaseModel."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """print the attributes in the module"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the 'updated_at' attribute with the current date and time."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        dict_cp = self.__dict__.copy()
        dict_cp['__class__'] = self.__class__.__name__
        dict_cp['created_at'] = self.created_at.isoformat()
        dict_cp['updated_at'] = self.updated_at.isoformat()
        return dict_cp
