#!/usr/bin/python3
"""Contains basemodel class"""
import uuid
import datetime


class Basemodel:
    "Basemodel class for all other classes"
    def __init__(self,id,created_at,updated_at):
        """Initializing base class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.date.today
        self.updated_at = datetime.date.today
    def __str__(self):
        """Method printing base class"""
        return '[{}] ({}) {}'.format()
    def save(self):
        return self.updated_at
    def to_dict(self):
        new_dict = self.__dict__
        new_dict.update({'__class__': self.__class__.__name__})
        new_dict.update({'created_at': self.created_at.isoformat()})
        new_dict.update({'updated_at': self.updated_at.isoformat()})

        return new_dict