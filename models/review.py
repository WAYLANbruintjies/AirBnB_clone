#!/usr/bin/python3
"""
Module for 'Review' class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A class that inherits from BaseModel that\
    represents user reviews
    """
    place_id = ""
    user_id = ""
    text = ""
