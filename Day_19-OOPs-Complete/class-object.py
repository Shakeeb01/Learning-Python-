# ***** CLASS *****

# Class in OOP is a blueprint.
# Every class has two main things:
# 1. Data or Property.       => Attributes
# 2. Functions or Behavior.  => Methods

# Basic Syntax of class.:
class Car:
    tyres = 8
    color = "blue" 
    
    
# ***** OBJECT *****
# Object is an instance of the class.
# this is how we create object of a class.
wagonr = Car()


# ************** Practical Implementation of class and object **************
# Methods are the functions that are written inside a class.

class Atm:
    # this "__init__" is a constructor.This will always execute when we will create an object from this class.
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()    
    
    def menu(self):
        user_input = input("""Hello,how would you like to proceed?
        Enter 1 to create pin
        Enter 2 to deposite
        Enter 3 to withdraw
        Enter 4 to check balance
        Enter 5 to exit
        
        """)
        
        if user_input == "1":
            print("create a pin.")
        elif user_input == "2":
            print("Deposite balance.")
        elif user_input == "3":
            print("withdraw")
        elif user_input == "4":
            print("Total balance.")
        elif user_input == "5":
            print("exiting.")
        else:
            print("invalid option.")                    
        

company = Atm()        