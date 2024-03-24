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
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        my_base_model = BaseModel()
        my_user = User()
        my_state = State()
        my_place = Place()
        my_city = City()
        my_amenity = Amenity()
        my_review = Review()
        models.storage.new(my_base_model)
        models.storage.new(my_user)
        models.storage.new(my_state)
        models.storage.new(my_place)
        models.storage.new(my_city)
        models.storage.new(my_amenity)
        models.storage.new(my_review)
        self.assertIn("BaseModel." + my_base_model.id, models.storage.all().keys())
        self.assertIn(my_base_model, models.storage.all().values())
        self.assertIn("User." + my_user.id, models.storage.all().keys())
        self.assertIn(my_user, models.storage.all().values())
        self.assertIn("State." + my_state.id, models.storage.all().keys())
        self.assertIn(my_state, models.storage.all().values())
        self.assertIn("Place." + my_place.id, models.storage.all().keys())
        self.assertIn(my_place, models.storage.all().values())
        self.assertIn("City." + my_city.id, models.storage.all().keys())
        self.assertIn(my_city, models.storage.all().values())
        self.assertIn("Amenity." + my_amenity.id, models.storage.all().keys())
        self.assertIn(my_amenity, models.storage.all().values())
        self.assertIn("Review." + my_review.id, models.storage.all().keys())
        self.assertIn(my_review, models.storage.all().values())


if __name__ == "__main__":
    unittest.main()
