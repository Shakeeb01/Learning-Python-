# A decorator in Python is a design pattern that allows you to add new functionality to an existing object without modifying its structure.

def my_decorator(func):
    def wrapper(*args,**kwargs): # this is the syntax which is used to take unlimited arguments.
        print(f"before the function is called.")
        func(*args,**kwargs)
        print(f"after the function is called.")
    return wrapper



@my_decorator
def example_function(name,greeting="Hello"):
    print(f"{greeting} {name}")

example_function("Shakeeb")