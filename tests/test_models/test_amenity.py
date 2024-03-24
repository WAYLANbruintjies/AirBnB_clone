#!/usr/bin/python3
"""
Unittests for Amenity model
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Testing Amenity class
    """

    def test_Amenity_inheritence(self):
        """
        Test if Amenity class inherits from BaseModel parent class
        """
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    def test_Amenity_attributes(self):
        """
        Test that Amenity class had name attribute
        """
        new_amenity = Amenity()
        self.assertTrue("name" in new_amenity.__dir__())

    def test_Amenity_attribute_type(self):
        """
        Test Amenity class for name attribute's type
        """
        new_amenity = Amenity()
        name_val = getattr(new_amenity, "name")
        self.assertIsInstance(name_val, str)
