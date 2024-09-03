# => Class:
# A class is a blueprint or a template for creating objects.


# Class Syntax:
class Person:
    name = "shakeeb"
    occupation = "Backend Developer"
    networth = 1000
    
    def info(self):
        print(f"User name is {self.name} and is a {self.occupation}.")



# => Object:
# Object is the instance of the class used to access the properties of the class.

New = Person()  # this is how we create any object from a class.
New.info()    
    
    
    
    
# => Self Parameter:
# The self parameter is a refernce to the current instance of the class,and is used to access the variables
# that belongs to the class. 