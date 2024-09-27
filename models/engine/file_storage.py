#!/usr/bin/python3
""" a module to serialize instancess to json files and vice versa"""
import json


class FileStorage():
    """a class for storing restoring data as json objects"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the __objects dictionary"""

        return self.__objects

    def new(self, obj):
        """adds an item to __objects dictionary"""

        class_name = obj.__class__.__name__
        obj_id = getattr(obj, "id", None)
        if obj_id is not None:
            item = "{}.{}".format(class_name, obj_id)
            self.__objects[item] = obj

    def save(self):
        """serializes __objects to JSON file"""

        og_obj = FileStorage.__objects
        ser_obj = {key: self.__objects[key].to_dict() for key in og_obj.keys()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(ser_obj, f)

    def reload(self):
        """deserializes JSON file to __objects"""

        try:
            from models.base_model import BaseModel
            with open(FileStorage.__file_path, 'r') as f:
                retrieved_data = json.load(f)
                for i in retrieved_data.values():
                    class_name = i['__class__']
                    del i['__class__']
                    self.new(eval(class_name)(**i))
        except FileNotFoundError:
            """this handles when there is no file found"""
            pass
