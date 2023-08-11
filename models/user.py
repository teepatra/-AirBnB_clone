#!/usr/bin/python3
"""Defines the review class."""
import models
from models.base_model import BaseModel

class User(BaseModel):
	"""Represent class user that inherit from BaseModel
	Attributes:
		email: (str) - user's email
		password: (str) - user's password
		first_name: (str) - user's first name
		second_name: (str) - user's second name
	"""
	email = ''
	password = ''
	first_name = ''
	last_name = ''
