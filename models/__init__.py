#!/usr/bin/python3
"""init file for the model package"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
