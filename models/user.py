#!/usr/bin/python3
"""user class
"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    """
    Inherits from BaseModel
    Public class attribute:
        email: (str)
        password: (str)
        first_name: (str)
        last_name: (str)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
