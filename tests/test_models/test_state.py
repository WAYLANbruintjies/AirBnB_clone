#!/usr/bin/python3
"""
Unittest for State model
"""

import os
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test to see if State inherits from BaseModel"""
    def test_State_inheritance(self):
        new_state = State
        self.assertIsInstance(new_state, BaseModel)

    def test_State_attributes(self):
        """
        Test that State class contains the attribute 'name'
        """
        new_state = State()
        self.assertTrue("name" in new_state.__dir__())

    def test_State_attributes_type(self):
        """
        Test that State class attribute name is of type str
        """
        new_state = State()
        name = getattr(new_state, "name")
        self.assertIsInstance(name, str)
