#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

storage = DBStorage() if os.getenv(
    'HBNB_TYPE_STORAGE') == 'db' else FileStorage()
""" FileStorage/DBStorage instance for all models. """
storage.reload()
# old file at the bottom
# storage = FileStorage()
# storage.reload()
