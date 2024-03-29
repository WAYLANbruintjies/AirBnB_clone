#!/usr/bin/python3
"""
Unittest for Review model
"""

import os
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test to see if Review Inherits from BaseModel"""
    def test_Review_inheritance(self):
        new_review = Review()
        self.assertIsInstance(new_review, BaseModel)

    def test_Review_attributes(self):
        """
        Test that Review class has the proper attributes in place
        namely -> place_id, user_id and text
        """
        new_review = Review()
        self.assertTrue("place_id" in new_review.__dir__())
        self.assertTrue("user_id" in new_review.__dir__())
        self.assertTrue("text" in new_review.__dir__())

    def test_Review_attributes_values_types(self):
        """
        Test that Review class has place_id, user_id and text
        attributes (not empty) and the type of each attribute
        """
        new_review = Review()
        place_id = getattr(new_review, "place_id")
        user_id = getattr(new_review, "user_id")
        text = getattr(new_review, "text")
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)
