#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

# Check the value of HBNB_TYPE_STORAGE environment variable
storage_type = os.getenv('HBNB_TYPE_STORAGE')

# Choose the appropriate storage class based on the value
if storage_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

# Load the data using the storage instance
storage.reload()

# storage = DBStorage() if os.getenv(
#     'HBNB_TYPE_STORAGE') == 'db' else FileStorage()
# """A unique FileStorage/DBStorage instance for all models.
# """
# storage.reload()
