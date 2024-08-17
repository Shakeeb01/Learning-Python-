# Python Decorators
# decorator is a design pattern that allows you to modify or extend the behavior of functions or methods without changing their actual code. Decorators are often used to add functionality to functions, such as logging, access control, memoization, or timing.
# Basic Example of a Decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func() # this function will be the argument of the main function.
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator # this is a decorator that will decorate the say_hello function.
def say_hello():
    print("Hello!")
say_hello()
 