#!/usr/bin/python3

import uuid
class BaseModel:
    def __init__(self, id=None):
        id = str(uuid.uuid4())
        self.id = id
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
