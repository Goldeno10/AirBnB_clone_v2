#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            dic_t = {}
            for k, v in FileStorage.__objects.items():
                if cls == v.__class__ or cls == v.__class__.__name__:
                    dic_t[k] = v
            return dic_t
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """ Serializes __objects to the JSON file
        (path: __file_path)
        """
        new_dict = {k: v.to_dict() for k, v in type(self).__objects.items()}
        with open(type(self).__file_path, "w") as f:
            json.dump(new_dict, f, indent=4)

    def delete(self, obj=None):
        """ Delete the current instance from the storage """
        if obj:
            key = f'{type(obj)}.{obj.id}'
            if key in self.__objects:
                del self.__objects[key]

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, does nothing
        """
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        if os.path.exists(type(self).__file_path) is True:
            with open(type(self).__file_path, "r") as f:
                for key, value in json.load(f).items():
                    self.new(eval(value["__class__"])(**value))

    def close(self):
        """ Calls the reload method """
        self.reload()
