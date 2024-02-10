#!/usr/bin/python3
'''City Module'''
from models.base_model import BaseModel


class City(BaseModel):
    ''' city Class.
    Attributes:
        name (str): ...
        state_id (str): ...
    '''
    state_id = ""
    name = ""
