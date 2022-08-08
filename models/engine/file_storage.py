#!/usr/bin/python3
""" Contains a Class File Storage that serialezes instances to a JSON 
    file and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Initializing class attributes:
        __file_path = JSON file path
        __objects = Basemodel instance dictionary
        structures of dictionary:
                obj.id: obj value"""

    __file_path = "file.json"
    __objects = dict() # we use a dictionary to avoid duplication of a key.When we save an object multiple times its not duplicated.

    def new(self, obj):
        """Adds a new basemodel instance in the __object dictionary"""
        FileStorage.__objects[obj.id] = obj
    
    def all(self):
        """Method returns all the methos stored in FileStorage"""
        return FileStorage.__objects


    def save(self):
        """Serializes the __objects dictionary values to the JSON file path"""
        new_dicts = [] #created a new list to store the dictionary of each of our objects because it helps avoid reduncdancy(repretitive information)
        for obj in FileStorage.__objects.values():
            new_dicts.append(obj.to_dict()) #list that contains the dictionary representation of each of our objects

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f: #writing to our JSON file
            json.dump(new_dicts, f)
    
    def reload(self):