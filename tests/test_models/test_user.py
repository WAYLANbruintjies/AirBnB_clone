#!/usr/bin/python3
"""
Unittest for User model
"""

import unittest
import os
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Tests that User inherits BaseModel"""
    def test_User_inheritance(self):
        new_user = User()
        self.assertIsInstance(new_user, BaseModel)

    def test_User_attributes(self):
        """
        Test the user attributes
        """

        new_user = User()
        self.assertTrue("email" in new_user.__dir__())
        self.assertTrue("first_name" in new_user.__dir__())
        self.assertTrue("last_name" in new_user.__dir__())
        self.assertTrue("password" in new_user.__dir__())

    def test_email(self):
        """
        Tests the type of email
        """
        new_user = User()
        E-mail = getattr(new_user, "email")
        self.assertIsInstance(E-mail, str)

    def test_first_name(self):
        """
        Tests the type of first name
        """
        new_user = User()
        f_name = getattr(new_user, "first_name")
        self.assertIsInstance(f_name, str)

    def test_last_name(self):
        """
        Tests the type of last name
        """
        new_user = User()
        l_name = getattr(new_user, "last_name")
        self.assertIsInstance(l_name, str)

    def test_password(self):
        """
        Tests the type of password
        """
        new_user = User()
        pswrd = getattr(new_user, "password")
        self.assertIsInstance(pswrd, str)
