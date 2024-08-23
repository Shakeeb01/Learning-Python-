# Inheritence

class Parent:  # this is super class.
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    def Showdetails(self):
        print(F"Parent name is {self.name} and {self.age} years old.")
        
        
Parent1 = Parent("Abdul Razzaq",54)
Parent1.Showdetails()         
            
class Child(Parent):  # this is sub class.
    def __init__(self, name, age,Country):
        super().__init__(name, age) 
        self.Country = Country
    def Showdetails(self):
        print(f"Child name is {self.name} and {self.age} years old.Lives in {self.Country}")
        
 
 
Child1 = Child("Shakeeb",22,"Pakistan")

Child1.Showdetails()        




# TYPES of inheritance:-

# 1. Single Inheritance        => A class inherits from a single parent class.
# 2. Multiple Inheritance      => A class can inherit from more than one parent class.
# 3. Multilevel Inheritance    => A class is derived from another derived class.
# 4. Hierarchical Inheritance  => Multiple classes inherit from the same parent class.
# 5. Hybrid Inheritance        => A combination of two or more types of inheritance.