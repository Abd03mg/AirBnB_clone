#!/usr/bin/python3
''' Review Module '''
from models.base_model import BaseModel


class Review(BaseModel):
    ''' Review Class.
    Attributes:
        place_id (str): ...
        user_id (str): ...
        test_id (str): ...
    '''

    place_id = ""
    user_id = ""
    text = ""
