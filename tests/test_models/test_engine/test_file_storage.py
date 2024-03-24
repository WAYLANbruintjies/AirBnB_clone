#!/usr/bin/python3
"""
Unittest for FileStorage module
"""

import unittest
import os
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.a = Amenity()
        self.b = BaseModel()
        self.c = City()
        self.p = Place()
        self.r = Review()
        self.s = State()
        self.u = User()
        self.storage = FileStorage()
        self.storage.save()
        if os.path.exits("file.json"):
            pass
        else:
            os.mknod("file.json")

    def tearDown(self):
        del self.a
        del self.b
        del self.c
        del self.p
        del self.r
        del self.s
        del self.u
        del self.storage
        if os.path.exits("file.json"):
            os.remove("file.json")

    def test_all(self):
        values = self.storage.all()
        self.asserIsNotNone(values)
        self.assertEqual(type(values), dict)

    def test_new(self):
        values = self.storage.all()
        self.u.name = "Ronaldo"
        self.u.id = "007"
        val2 = self.storage.new(self.u)
        key = "{}.{}".format(self.u.__class__.__name__, self.u.id)
        self.assertIsNotNone(value[key])

if __name__ == "__main__":
    unittest.main()
