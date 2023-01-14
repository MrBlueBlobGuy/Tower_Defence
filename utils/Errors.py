import sys


class ObjectTypeError(Exception):
    """If the type of object is not valid this error is raised"""
    def __init__(self):
        super().__init__("ObjectTypeError: Object file provided is not a valid file")
        sys.exit(-1)


class InputError(Exception):
    def __init__(self):
        super().__init__("InputError: Input Axis config provided is not valid")
        sys.exit(-1)
