# Inheritence
# when a child class is derived from the main class.that child class can access all the attributes and methods of
# parent class using inheritence.

# TYPES OF INHERITENCE :- 
# 1. Single inheritence  => A class inherits from one parent class.
# 2. Multiple inheritence =>  A class inherits from more than one parent class.
# 3. Multilevel inheritence  => A class inherits from a child class, making the child class a parent for another class.
# 4. Hierarchial inheritence  => Multiple classes inherit from the same parent class.
# 5. Hybrid inheritence => A combination of two or more types of inheritance, typically involving multiple inheritance and hierarchical inheritance.

class Person:
    def __init__(self,Name,Age,Occupation):
        self.Name = Name
        self.Age = Age
        self.Occupation = Occupation
        
    def showDetail(self):
        print(f"{self.Name} is {self.Occupation} and {self.Age} years old. ")
        
        

Programmer1 = Person("Shakeeb",22,"Developer")
Programmer1.showDetail()
# this is inheritence. 
class Programmer(Person):
    def __init__(self,Name,Age,Occupation,Pay):
        super().__init__(Name, Age, Occupation)  #this super keyword will  Call the parent class constructor.
        self.Pay = Pay
        
    def showProgrammer(self):
        print(f"{self.Name} is {self.Occupation} and {self.Age} years old.And Earns {self.Pay} a month. ")
        
        
Programmer2 = Programmer("Ronaldo",23,"Python Developer",10000)      
Programmer2.showProgrammer()
           