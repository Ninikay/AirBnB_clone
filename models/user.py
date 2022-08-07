#!/usr/bin/python3
"This class inherits from the BaseModel class"
from models.base_model import BaseModel


class User(BaseModel):
    """The User class is a child class of BaseModel
    Public Class Attributes:
        email = ""
        last_name = ""
        first_name = ""
        password = ""
    """
    email = ""
    last_name = ""
    first_name = ""
    password = ""
