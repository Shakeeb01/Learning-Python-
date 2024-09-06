# => Inheritence in python 
# When a class derived from another class.The child class will inherit all the public and protected properties
# and methods of the parent class.


# => Types of inheritence:
# 1. Single inheritence
# 2. Multiple inheritence
# 3. Multilevel inheritence
# 4. Hierarchial inheritence
# 5. Hybrid inheritence


# # => Syntax
class Employee:
    def __init__(self,name,age,salary):
        self.name = name 
        self.age = age
        self.salary = salary
    
    def show_info(self):
        print(f"Our new employee name is {self.name} and he/she {self.age} years old.")    
        
        
class Programmer(Employee):
    def show_occupation(self):
        print(f"{self.name}  is Programmer.And Earns ${self.salary} a year.")
        

first = Employee("Shakeeb",22,1000)
first.show_info()
NewEmp = Programmer("Shakeeb",22,1000)
NewEmp.show_occupation()        


# => Single Inheritence:
# In single inheritance, a child class inherits from only one parent class.
class Parent:
    pass
class Child(Parent):
    pass




# =>  Multiple Inheritence:
# In multiple inheritance, a child class inherits from more than one parent class.
class Dad:
    pass
class Mom:
    pass
class Child(Dad,Mom):
    pass




# => Multilevel Inheritence:
# In multilevel inheritance, a child class inherits from a parent class, which itself is a child of another class.
class GrandeFather:
    pass
class Father(GrandeFather):
    pass
class Son(Father):
    pass 




# => Hierarchical Inheritance
# In hierarchical inheritance, multiple child classes inherit from the same parent class.

class Parent:
    pass
class Child1(Parent):
    pass
class Child2(Parent):
    pass


# => Hybrid Inheritance
# Hybrid inheritance is a combination of two or more types of inheritance. It typically includes multiple and multilevel inheritance.
class Parent:
    def show(self):
        print("This is the Parent class")

class Child1(Parent):
    def display1(self):
        print("This is Child1 class")

class Child2(Parent):
    def display2(self):
        print("This is Child2 class")

class GrandChild(Child1, Child2):
    def display(self):
        print("This is GrandChild class")

obj = GrandChild()
obj.show()    # Inherited from Parent
obj.display1()  # Inherited from Child1
obj.display()   # GrandChild method
