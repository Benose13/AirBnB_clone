#!/usr/bin/python3

import uuid
import models
from datetime import datetime


class BaseModel():
    """
    Defining a super class BaseModel which other classes
    can inherit these common attributes and methods
    and have the functionality described.


    """
    def __init__(self, *args, **kwargs):
        """
        Initialize BaseModel class
        """
        if kwargs:
            if kwargs["__class__"] == self.__class__.__name__:
                self.id, self.created_at, self.updated_at, *_ = kwargs.values()
                self.created_at = datetime.strptime(
                        self.created_at, "%Y-%m-%dT%H:%M:%S.%f"
                        )
                self.updated_at = datetime.strptime(
                        self.updated_at, "%Y-%m-%dT%H:%M:%S.%f"
                        )
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        models.storage.new(self)

    def save(self):
        """
        Updates the public instance attribute
        'updated_at' with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the object's attributes.
        """
        dict_cp = self.__dict__.copy()
        dict_cp['__class__'] = self.__class__.__name__
        dict_cp['created_at'] = self.created_at.isoformat()
        dict_cp['updated_at'] = self.updated_at.isoformat()
        return dict_cp

    def __str__(self):
        """
        Return the string representation of the class for the user.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
