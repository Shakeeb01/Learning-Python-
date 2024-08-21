#  getters and setters are methods used to access and modify the private attributes of a class. While Python allows direct access to attributes, using getters and setters can help enforce encapsulation, control access, and add validation.

class Person:
    def __init__(self, name):
        self._name = name  # this is  private attribute
    
    # this is getter method.
    @property    # This decorator is used to define a method as a getter, allowing it to be accessed like an attribute.
    def get_name(self):
       return self._name
    
    # this is  Setter method.
    @get_name.setter   #This decorator defines the setter method for the name attribute, enabling attribute assignment with validation.
    def set_name(self, name):
            self._name = name

# Usage
User1 = Person("John")
print(User1.get_name) 
User1.set_name = "Doe"
print(User1.set_name) 
        
         