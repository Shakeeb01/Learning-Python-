# polymorphism refers to the ability of different objects to respond to the same method in a way  
# appropriate to their class.

class Animal:
    def __init__(self,name):
        self.name = name
    def showname(self):
        print(self.name)



class Human:
    def __init__(self,name):
        self.name = name       
    def showname(self):
        print(self.name)
        
        
animal1 = Animal("Lion")
human1 = Human("Shakeeb")

animal1.showname()        
human1.showname()        