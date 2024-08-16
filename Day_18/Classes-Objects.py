# Python Class and Object
# A class is a blueprint or a template for creating objects.providing initials values for state
# and implementations of behavior. the user defined objects are created using class keyword.

# Lets now create  a class using the "class" keyword.

class person: #this is how we create class.
    name = "Shakeeb"
    occupation = "Python Developer"
    age = 22
    def info(self): # this "self" parameter is a reference to the current instance of the class.
        print(f"{self.name} is a {self.occupation}.")
    
a = person() # this is how we create object from class.
print(f"{a.name} is {a.age} years old.")    

a.info()