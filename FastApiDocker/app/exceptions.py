from fastapi import status
from typing import Optional

class ModelInfoException(Exception):
    pass

class ModelInfoNotFoundError(ModelInfoException):
    def __init__(self, model: Optional[str] = None):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = model + "Info not found"

class ModelInfoAlreadyExistError(ModelInfoException):
    def __init__(self, model: Optional[str] = None):
        self.status_code = status.HTTP_409_CONFLICT
        self.detail = model + "Info Already Exists"
    