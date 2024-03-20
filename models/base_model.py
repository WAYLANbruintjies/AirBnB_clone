#!/usr/bin/python3
"""
A parent class that defines all common attributes/methods for other classes,
BaseModel - module
"""

from datetime import datetime
import uuid
import models

class BaseModel:
    """
    Initialisation of BaseModel class
    """
    def __init__(self, *args, **kwargs):
        display_time = "%Y-%m-%dT%H:%M:%S.f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, display_time))
                else:
                    setattr(self, key, value)

        models.storage.new(self)

    def __repr__(self):
        """
        Same purpose as '__str__' to represent a BaseModel instance
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def __str__(self):
        """
        String representation of BaseModel instance
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Updates public instance attribute 'updated_at' with current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Dictionary representation of BaseModel class"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.updated_at.isoformat()
        new_dict['updated_at'] = self.created_at.isoformat()

        return new_dict

if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
