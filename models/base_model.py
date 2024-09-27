#!/usr/bin/python3
"""a model representing a base through a class"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """a representation of a base"""

    def __init__(self, *args, **kwargs):

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    """set the created_at and updated_at as datetime objects"""

                    setattr(self,
                            key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                            )
                elif key == '__class__':
                    continue
                else:
                    """set other values as usual using setattr method"""

                    setattr(self, key, value)
        else:
            """this creates a usual class instance as used earlier"""

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__)

    def save(self):
        """updates the updated_at variable"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary representation of the class"""
        obj = self.__dict__.copy()

        obj['__class__'] = self.__class__.__name__

        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()

        return obj
