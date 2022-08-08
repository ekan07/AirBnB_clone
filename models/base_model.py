#!/usr/bin/python3
"""Contains basemodel class which is the base class for all other 
classes to be used in Airbnb project"""
import uuid
from datetime import datetime,timezone


class BaseModel:
    "Basemodel class for all other classes"
    def __init__(self):
        """Initializing Model base class 
        Attributes:
        id (str): It's a UUID for the instance created.
        created_at (datetime): The current date and time that
            an instance is created.
        updated_at (datetime): The current date and time that
            an instance is created and it will be updated every
            time that the object is changed.
        """     
        self.id = str(uuid.uuid4())

        now = datetime.now(timezone.utc)
        self.created_at = now
        self.updated_at = now
    
    def __str__(self):
        """Method printing base class"""
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self): #method that allows us to save an object
        """Method updates and saves the updated_at attribute with current datetime"""
        self.updated_at = datetime.now(timezone.utc)
        
    def to_dict(self): #here we want our instances of this class dictionary to contain the name of their class and date they were created and date they were updated
        """Method to generate a dictionary representation of an instance"""
        new_dict = dict()
        new_dict['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key in ('created_at', 'updated_at'):
                new_dict[key] = self.updated_at.isoformat()        
            else:
                new_dict[key] = value
        return new_dict