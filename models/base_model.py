#!/usr/bin/python3
"""import unique id and date time"""


import uuid
import datetime

"""Create a BaseModel class"""


class BaseModel:
    """Constructor to contain public instances"""
    def __init__(self):
        """id, created_at, updated_at instances created"""
        id = str(uuid.uuid4())
        self.id = id
        created_at = datetime.datetime.now()
        created_at = str(created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        self.created_at = created_at
        self.updated_at = created_at

    def save(self):
        """update time when saving"""
        updated_at = datetime.datetime.now()
        updated_at = str(updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        self.updated_at = updated_at
        return self.updated_at

    def to_dict(self):
        """return dictionary of class for json"""
        dict1 = self.__dict__
        dict1["__class__"] = self.__class__.__name__
        return dict1

    def __str__(self):
        """return print out"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
