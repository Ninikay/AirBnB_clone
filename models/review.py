#!/usr/bin/python3
""" Review class inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Child of BaseModels with
    Public attributes:
    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
