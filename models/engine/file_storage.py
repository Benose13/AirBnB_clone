#!/usr/bin/python3
"""Class FileStorage"""
import os
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
        ry:
            with open(self.__file_path, 'r') as file:
                content = file.read()
                if not content:
                    return

            objects_dict = json.loads(content)

            for key, value in objects_dict.items():
                class_name, obj_id = key.split(".")

                if class_name in class_names:
                    obj_class = class_names[class_name]
                    deserialized_obj = obj_class(**value)
                    obj_key = "{}.{}".format(class_name, obj_id)
                    self.__objects[obj_key] = deserialized_obj
        except FileNotFoundError:
            pass
