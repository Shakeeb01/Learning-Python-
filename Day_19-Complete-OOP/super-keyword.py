# the super() keyword is used to call a method from a parent class. It’s particularly useful when you are working with inheritance. 

class Parent:
    # parent constructor.
    def __init__(self,name):
        self.name = name
        
    # parent class method
    def showDetail(self):
        print(f"Parent name is {self.name}")
        
        
class Child(Parent):
    # child constructor.
    def __init__(self,name,age):
        super().__init__(name)  # Call the parent class's __init__ method
        self.age = age
    # method inherit from parent. 
    def showDetail(self):
        print(f"Child name is {self.name} and {self.age} years old.")
        
        
parent = Parent("Abdul Razzaq")
parent.showDetail()  

child = Child("Shakeeb",22)
child.showDetail()
        
                