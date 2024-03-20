#!/usr/bin/python3
"""
Module for 'City' class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    A class that inherits from BaseModel that\
    represents different cities by name and id
    """
    state_id = ""
    name = ""
