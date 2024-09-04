# => Inheritence in python 
# When a class derived from another class.The child class will inherit all the public and protected properties
# and methods of the parent class.


# => Types of inheritence:
# 1. Single inheritence
# 2. Multiple inheritence
# 3. Multilevel inheritence
# 4. Hierarchial inheritence
# 5. Hybrid inheritence


# => Syntax
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