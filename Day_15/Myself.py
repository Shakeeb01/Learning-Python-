def welcome():
    print("hey you are welcome from shakeeb.")
    
   
   
# In Python, the statement if __name__ == "__main__": is used to determine if a script is being run as the main program or if it is being imported as a module in another script.    

#Common Use Case:
# This construct is commonly used to include test code or a main function that should only run when the script is executed directly, and not when the script is imported as a module elsewhere.

if __name__ == "__main__":
 welcome()    
 
print(__name__) 