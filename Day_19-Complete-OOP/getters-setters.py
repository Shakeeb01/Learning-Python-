# getters and setters are methods used to access and modify the attributes of a class, typically used to control access to private or protected variables. 

# => Example without decorator:
class Person:
    def __init__(self,name):
        self._name = name # _name is now "protected attribute."
        
    # Getter Method
    # this method is to get the value of name.
    def get_name(self):
        return self._name
    
    # Setter Method
    # this method is to change or set the new name.
    def set_name(self,name):
        self._name = name
        
        
        
# Usage 
p1 = Person("Shakeeb")    #created the object from the 'Person' class.
p1.set_name('Ronaldo')
print(p1.get_name())       
        
        
        
# => Example using '@property' decorator.
class Person:
    def __init__(self, name):
        self._name = name  # _name is a "protected" attribute

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


# Usage
p = Person("John")
print(p.name)  # Access name using property (like an attribute)
p.name = "Doe"  # Modify name using setter
print(p.name)
  