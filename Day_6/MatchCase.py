Num = int(input("Guess the number between 0 to 5: "))

match Num: # this is where we tell which variable is to match.
    
    case 0:   # this is condition 1
        print("Wrong")
    case  1:   #this is condition 2 and so on...
        print("Wrong")
    case  2:
        print("Wrong")
    case  3:
        print("Wrong")        
    case  4:
        print("Correct")
    case  5:
        print("Wrong")        
    case _ if Num>5:   #this is default
        print("Invalid Number")    
        
        