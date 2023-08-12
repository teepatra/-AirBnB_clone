#!/usr/bin/env python3
""" Class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Public class attributes:

    place_id: string - (str): Place.id
    user_id: string - (str): User.id
    text: string - (str): text of the review
    """
    place_id = ""
    user_id = ""
    text = ""
