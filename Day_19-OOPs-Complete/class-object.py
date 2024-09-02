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
    
    # this is to create pin
    def create_pin(self):
        self.pin = input("Enter your pin.")
        print("Pin set successfully! ")
        
    # this is to deposite 
    def deposite(self):
        temp = input("Enter your pin.")
        if temp == self.pin:
            deposite_amount = int(input("Enter the amount."))
            self.balance+=deposite_amount
            print("Deposite Successfull!")
        else:
            print("Invalid pin.")    
            
    #  this is to withdraw
    def withdraw(self):
        temp = input("Enter your pin.")
        if temp == self.pin:
            withdraw_amount = int(input("Enter the amount."))
            if withdraw_amount < self.balance:
                self.balance-=withdraw_amount 
                print("Withdraw successfull!")
            else:
                print("insuficients balance.")
        else:
            print("invalid pin.")        
            
    # this is check total balance.
    def check_balance(self):
        temp = input("Enter your pin.")
        if temp == self.pin:
            print(self.balance)
        else:
            print("invalid pin.")    
         
        
    
               
    def menu(self):
        user_input = input("""Hello,how would you like to proceed?
        Enter 1 to create pin 
        Enter 2 to deposite
        Enter 3 to withdraw
        Enter 4 to check balance
        Enter 5 to exit
        
        """)
        
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposite()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            print("Goodbye!")
            
        else:
            print("invalid option.")                    
        
    
company = Atm()      
company.deposite()  