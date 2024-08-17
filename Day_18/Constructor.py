class Person:
    # this init is a constructor.
    def __init__(self,name,age): # this function will always invoked when we will create new object from this class.
        self.name = name
        self.age = age
        
        
First  = Person("Shakeeb",22)        
Second  = Person("Shah",23)        

print(First.name)
print(Second.age)

# Two types of constructor.

# 1. Parameterized Constructor.
class Animale():
    def __init__(self,voice):
        self.voice = voice
        
        
# 2. Default Constructor.
class Student():
    def __init__(self):
        print("this is default construtor.")
    