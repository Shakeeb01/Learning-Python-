# A Construtor is a special method in a class used to create and initialize an object of a class.
# Construtor is invoked automatically when an object of a class is created.

# => Syntax of python Construtor:

def __init__(self):
    # initialization.
    pass


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
        
    def showdetail(self):
        print(f"{self.name} is {self.age} years old.")


first_person = Person("Shakeeb",22)            
first_person.showdetail()


Second_person = Person("Ronaldo",37)            
Second_person.showdetail()



# => Two types of construtor:

# 1. Parameterized Construtor
# When the constructor accepts the arguments along with self,it is know as  parameterized construtor.

# 2. Default  Construtor
# When the construtor does not accept any arguments except self.it is know as default construtor.