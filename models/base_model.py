#!/usr/bin/python3
''' define uuid and datetime classes.'''
import models
ud = __import__("uuid")
dt = __import__("datetime").datetime


class BaseModel:
    ''' Base Model class that other classes inherits from it.
        Attributes:
            id: assign with uuid when instance is created.
            created_at: datetime when instance is created.
            updated_at: date time when instance time will be updated.
        Args:
            *args: used to verify that is unknown number of argument
                    will be passed.
            **kwargs: used to verify that is unknown number of key word
                    arguments will be passed.
    '''
    __timef = "%Y-%m-%dT%H:%M:%S.%f"
    def __init__(self, *args, **kwargs):

        if kwargs:
            for key, val in kwargs.items():
                if key == "__class__":
                    continue
                if key in {"created_at", "updated_at"}:
                    self.__dict__[key] = dt.strptime(val, self.__timef)
                else:
                    self.__dict__[key] = val
        else:
            self.id = str(ud.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            models.storage.new(self)

    def save(self):
        ''' function that updates the \"updated_at attribute\". '''
        self.updated_at = dt.now()
        models.storage.save()

    def to_dict(self):
        ''' returns a dictionary containing all
        keys/values of __dict__ of the instance.
        Return:
            di:....
        '''
        di = self.__dict__.copy()
        di["__class__"] = self.__class__.__name__
        di["created_at"] = self.created_at.isoformat()
        di["updated_at"] = self.updated_at.isoformat()
        return di

    def __str__(self):
        ''' string representation of class.
        Return:
            [<class name>] (<self.id>) <self.__dict__> format of class.
        '''
        c_na = self.__class__.__name__
        st = "[{}] ({}) {}".format(c_na, self.id, self.__dict__)
        return st
