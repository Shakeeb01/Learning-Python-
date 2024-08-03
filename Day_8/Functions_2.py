#Functions arguments and return statements.
# Ther are four types of arguments:-
# 1. Default Arguments
# 2. Keywords Arguments
# 3. Variable length Arguments
# 4. Required Arguments


def add(a=10,b=20):  #these are default arguments.
    print(a+b)
    
add(b=40,a=60)  #these are keyword arguments    



#these is the  required arguments 
def add(a,b,c=100):  
    print(a+b+c)
    
add(50,60)   