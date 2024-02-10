#!/usr/bin/python3
''' Define BaseModel class. '''
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    ''' FileStorage class that uses to store basemodel INFOs to external file.
    Attribute:
        __file_path: path to json file.
        __objects: stores all objects by "ID".
    '''
    __file_path = "AP.json"
    __objects = dict()

    def all(self):
        ''' function that return all objects.
        Return:
            __objects
        '''
        return self.__objects

    def new(self, obj):
        ''' function that sets in __onject the obj with key "<obj class name>.id".'''
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        ''' function that saves object INFOs to JSON file.'''
        js_ob = {}
        for i in self.__objects:
            js_ob[i] = self.__objects[i].to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(js_ob, f)

    def reload(self):
        ''' method that deserializes JSON file. '''
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for _ in json.load(f).values():
                    clas = _["__class__"]
                    del _["__class__"]
                    self.new(eval(clas)(**_))
        except FileNotFoundError:
            pass
