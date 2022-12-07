import inspect
from liasis.errors import *


__all__ = [
    "Parameters",
]


class Parameters:
    def __init__(self, function, **ext_kwargs: any):
        self.ext_kwargs = ext_kwargs
        self.function = function

    def evaluate(self, *args: any, **kwargs: any) -> None:
        inspection = inspect.signature(self.function).parameters
        for element in inspection:
            if self.ext_kwargs.get(element) == None and element != "self":
                raise NoTypeDefinition(element)

        for idx, (k, v) in enumerate(self.ext_kwargs.items()):
            if k != "return_value":
                self_sub = 0
                for ins_idx, i in enumerate(inspection):
                    if i == "self" and self_sub == 0:
                        self_sub = 1
                        continue

                    if i == k and ins_idx - self_sub != idx:
                        raise InvalidParameterPosition(k)

                if v != type(args[idx + self_sub]):
                    raise InvalidArgumentType(
                              actual=type(args[idx]),
                              argument=k,
                              expected=v
                          )

        result = self.function(*args, **kwargs)

        if "return_value" not in self.ext_kwargs and result is not None:
            raise InvalidReturnType(
                      actual=type(result),
                      argument=self.function.__name__,
                      expected=type(None)
                  )
        elif ("return_value" in self.ext_kwargs and
            self.ext_kwargs["return_value"] != type(result)):
            raise InvalidReturnType(
                      actual=type(result),
                      argument=self.function.__name__,
                      expected=self.ext_kwargs["return_value"]
                  )

        return result

