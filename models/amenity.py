#!/usr/bin/python3
""" Amenity class inherits from BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Child of BaseModels with
    Public attributes:
    name: string - empty string
    """
    name = ""
