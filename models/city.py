#!/usr/bin/python3
""" City class inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Child of BaseModels with
    Public attributes:
    state_id: string - empty string: it will be the State.id
    name: string - empty string
    """
    state_id = ""
    name = ""
