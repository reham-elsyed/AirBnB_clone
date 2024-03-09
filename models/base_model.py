#!/usr/bin/python3
"""Create class"""
import json
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Class method basemodel"""

    def __init__(self, *args, **kwargs):
        """Constructor create

        Args:
            id: unique id to eeach base model.
            created_at: time when obj is created.
            updated_at: time when obj is updated.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v, time_format))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        storage.new(self)

    def save(self):
        """
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        """
        base_dict = self.__dict__.copy()
        base_dict["__class__"] = self.__class__.__name__
        base_dict["created_at"] = self.created_at.isoformat()
        base_dict["updated_at"] = self.updated_at.isoformat()
        return base_dict

    def __str__(self):
        """
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
