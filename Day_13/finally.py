 # Finally Clause
 
try:
    l = [2,3,434,5646,353534545]
    i = int(input("Enter the index : "))
    print(l[i])
except:
    print("Invalid index")
finally:
    print("Finally clause is always executed.")    
        