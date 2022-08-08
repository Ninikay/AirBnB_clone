#!/usr/bin/python3
""" State class inherits from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """Child of BaseModels with
    Public attributes:
    name: string - empty string
    """
    name = ""
