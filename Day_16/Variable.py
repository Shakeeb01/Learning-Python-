x = 4 # this is global variable.which means we can access this in any programm.
print(f"this is global variable {x}")
def hello():
    global x  # this is to change the value of global variable.
    x = 5   # this is local variable means this can be access on in the function.
    print(f"this is local variable {x}")
    y = "shah"  # we can access this outside the function.
    
hello()    

print(f"this is global variable {x}")