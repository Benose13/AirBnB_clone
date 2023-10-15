#!/usr/bin/python3
"""Class FileStorage"""
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """class that serializes instances to a JSON file and deserializes JSON"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ put key(class name.id) and obj value in obj dic"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serialize a dic"""
        data = {}
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """deserialize json"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
