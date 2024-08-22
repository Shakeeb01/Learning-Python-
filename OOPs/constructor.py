class Person:
    # this is a constructor.this constructor will be automatically invoked always.
    def __init__(self,name,age,country):
        # the self keywrod targets the object that is created using class.
        self.name = name 
        self.age = age 
        self.country = country
    #this is now object method.    
    def hello(self):
        print("hello")

Person1 = Person("Shah",22,"Pakistan")     
print(Person1.name)

Person1.hello()