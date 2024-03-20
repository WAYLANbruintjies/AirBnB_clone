#!/usr/bin/python3
"""
__init__ python file for models folder/directory, initialising packages for models/
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
