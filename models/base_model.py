#!/usr/bin/python3
"""
    This module is the base class for all
    other modules for the hbnb clone project.
    i.e Most modules will inherit from this class.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    id: uses RFC4122 to generate ids for an instance
    """

    def __init__(self, *args, **kwargs):
        """ Initialization function for the BaseModel class"""

        if kwargs != {}:
            kwargs["created_at"] = datetime.fromisoformat(
                kwargs["created_at"])

            kwargs["updated_at"] = datetime.fromisoformat(
                kwargs["updated_at"])

            for (key, values) in kwargs.items():
                if key != "__class__":
                    setattr(self, key, values)
        else:
            id = uuid.uuid4()
            self.id = str(id)
            d = datetime(1, 1, 1).now()
            self.created_at = d
            self.updated_at = d
            models.storage.new(self)

    def __str__(self):
        """ Non formal representation of instance used for printing """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ Saves the instance object to json file"""
        d = datetime(1, 1, 1).now()
        self.updated_at = d
        models.storage.save()

    def to_dict(self):
        """ Converts the instance object to dictionary objects"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()

        return my_dict
