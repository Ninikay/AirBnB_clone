#!/usr/bin/python3
"""This module serializes instances into JSON and
    can also deserialize JSON back to instances
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """ This class converts instances from a basemodel
        to JSON and can also deserialize back to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        """
            writes the object to the class dict __objects
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
            serializes the object to json
        """
        deserialized_json = {}
        for (key, obj) in FileStorage.__objects.items():
            deserialized_json[key] = obj.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding="utf-8") as f:
            json.dump(deserialized_json, f, indent=2)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file\
             (__file_path) exists ; otherwise, do nothing. If the file \
                does not exist, no exception should be raised)

        """
        if os.path.exists(self.__file_path):
            with open(FileStorage.__file_path, mode="r", encoding="utf-8")\
                    as f:
                deserialized_json = json.load(f)
            for key, value in deserialized_json.items():
                class_name = key.split(".")
                FileStorage.__objects[key] = globals()[class_name[0]](**value)
