# Exception classes


__all__ = [
    "InvalidParameterPosition",
    "InvalidArgumentType",
    "InvalidReturnType",
    "NoTypeDefinition",
]


class InvalidParameterPosition(Exception):
    def __init__(self, element):
        message = f"The parameter {element} is positioned incorrectly."
        super().__init__(message)


class InvalidArgumentType(TypeError):
    def __init__(self, argument=None, actual=None, expected=None):
        message = f"Expected {argument} to be {expected} but got {actual}."
        super().__init__(message)


class InvalidReturnType(TypeError):
    def __init__(self, argument=None, actual=None, expected=None):
        message = f"Expected {argument} to return {expected} but got {actual}."
        super().__init__(message)


class NoTypeDefinition(TypeError):
    def __init__(self, element):
        message = f"The parameter {element} has no type definition."
        super().__init__(message)

