import functools
from liasis.core import *


# Liasis adds static-type checking to functions and methods through
# a decorator.


__version__ = "0.1.0"
__all__ = ["Typed"]


class Typed:
    @classmethod
    def func(cls, **ext_kwargs: any) -> Parameters:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args: any, **kwargs: any):
                parameters = Parameters(func, **ext_kwargs)
                return parameters.evaluate(*args, **kwargs)
            return wrapper
        return decorator

