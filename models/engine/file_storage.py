#!/usr/bin/python3
"""Class FileStorage"""
import os
import json
from models.base_model import BaseModel


class FileStorage:
    def __init__(self, file_path="file.json"):
        """Initialize a FileStorage instance with a given file path."""
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set an object in __objects with the key <class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """Deserialize the JSON file to __objects (if it exists)."""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_ = globals()[class_name]
                    instance = class_(**value)
                    self.__objects[key] = instance
