#!/usr/bin/python3
"""
Class for serialization and deserialization of dictionaries
"""
import json
from os.path import isfile


class FileStorage:
    """Class for serialization and deserialization"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Method to return getter"""
        return FileStorage.__objects

    def new(self, obj):
        """Setter for objects attribute"""
        if obj is not None:
            k = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[k] = obj

    def save(self):
        """
            Method to serialize dictionary of data, use to_dict method to return format of dict
        """
        obj_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
            method to deserialize json dict to python object.
            repopulate the objects attribute with k,v pairs after deserializing json
        """
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    f_cont = f.read()
                    obj_dict = json.loads(f_cont)
                    obj_dict = {k: self.classes() [v["__class__"]] (**v) for k, v in obj_dict.items()}
                    FileStorage.__objects = obj_dict
                except:
                    pass


    def classes(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from  models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review


        classes = {
                "BaseModel" : BaseModel,
                "User" : User,
                "State" : State,
                "City" : City,
                "Aminety" : Amenity,
                "Place" : Place,
                "Review" : Review
                }
        return classes
