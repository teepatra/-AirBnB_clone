#!/usr/bin/python3
"""
BaseModel class file
"""

from datetime import datetime
import uuid
import models


class BaseModel:
    """Defines all attributes/methods that are common in all classes"""

    def __init__(self, *args, **kwargs):
        """instantiates a new object """

        t = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == 'updated_at':
                        setattr(self, key, datetime.strptime(value, t))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """Returns string representation of the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
	 """ updates the public instance attribute updated_at with current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return a new dictionnary representation of the class"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat((sep='T')
        new_dict['updated_at'] = self.updated_at.isoformat((sep='T')
        return new_dict
