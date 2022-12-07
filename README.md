## LIASIS

Liasis is a package that utilizes Python's type annotation and decorator to add
static-type checking to functions.

```py
from liasis import Typed

@Typed.func(name=str, return_value=str)
def message(name):
    print (f"The value passed is {name}")

message("Hello World!")
```
Result:
```bash
liasis.errors.InvalidReturnType: Expected message to return <class 'str'> but got <class 'NoneType'>
```

The arguments in the decorator are _order-sensitive_ which means they
should match the order of the arguments in the function being type-checked. For
class functions, the `self` is ignored but the rule applies to the next arguments:

```py
class Message:
    @Typed.func(content=str)
    def out(self, content):
        print(f"Displaying message: f{content}")

Message().out("Hello World!") # this will not result to error
```

### NOTE
This project is for educational purposes only.

