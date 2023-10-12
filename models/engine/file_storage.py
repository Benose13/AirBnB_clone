#!/usr/bin/python3
"""Class FileStorage"""
import os
import json
from models.base_model import BaseModel


class FileStorage:
    """class that serializes instances to a JSON file and deserializes JSON"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return __objects"""
        return self.__objects

    def new(self, obj):
        """ put key(class name.id) and obj value in obj dic"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serialize a dic"""
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """deserialize json"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_ = globals()[class_name]

                    self.__objects[key] = class_(**value)
