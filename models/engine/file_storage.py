#!/usr/bin/python3
"""FileStorage Module"""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import json
import os


class FileStorage:
    """
    FileStorage class for storing, serializing and deserializing data
    """
    __file_path = "file.json"

    __objects = {}

    def new(self, obj):
        """
        Sets an object in the __objects dictionary whereas\
        key = <obj class name>.id
        """
        obj_class_name = obj.__class__.__name__

        key = "{}.{}".format(obj_class_name, obj.id)

        FileStorage.__objects[key] = obj


    def all(self):
        """
        Returns the __objects dictionary,\
        providing access to all the stored objects
        """
        return  FileStorage.__objects


    def save(self):
        """
        Serialises __objects dictionary into JSON format\
        and saves it to the file specified by __file_path
        """
        all_objs = FileStorage.__objects

        obj_dict = {}

        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Method to deserialise JSON file
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                try:
                    obj_dict = json.load(f)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')

                        new = eval(class_name)

                        inst = new(**value)

                        FileStorage.__objects[key] = inst
                except Exception:
                    pass
