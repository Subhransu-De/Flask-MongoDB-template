from app.exception.core_exception import CoreException


class NotFoundException(CoreException):
    def __init__(self, message):
        super().__init__(message)
