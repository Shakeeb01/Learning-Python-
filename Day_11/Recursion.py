# Recursion in Python is a programming technique where a function calls itself in order to solve smaller instances of the same problem

def factorial(num):
    if(num == 1 or num==0):
         # Base start
        return 1
    else:
        # Recursion state.
        return num * factorial(num-1)

print(factorial(5))       


def fibonacci(n):
    # Base cases
    if (n == 0 or n ==1):
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))
  