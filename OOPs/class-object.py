# this is how we create class.first use "class" keyword then class name with first letter capital.
class Factory:
    pass
# class attribute:

class Person:
    name = "shah" # this name is now class attribute.we can not call this now variable.
    
# class method:
class Car:
    def hello():  # this is now class method.
        pass    
    
    
    
class Practice:
    # when we create private attribute or methods, This is encapsulation.
    
    # if we want to private any attribute we use two underscore before the attribute.
    __age = 18 #this age is now private attribute.which mean we can not access this outside the class.
    
    def __sayhello(): # this is now private method after using two underscore before method name.
        print("hello")
    __sayhello()

Practice()    
        



# *** Objects ***
# when we call a class using varibale.Now that varibale is object of our class.

class Person:
    name = 'shah'
    
obj  = Person() # this is how we create an object of a class.
