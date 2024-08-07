a = input("Enter the number for multiplication table : ")

try:
    for i in range(1,11):
     print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print(f"invalid input '{a}' ")
    
print("Some important lines of code.") 
    
# ******** Custom Erros ***********
 
num = int(input("Enter the number between 5 to 10"))

if(num < 5 or num > 10):
    raise ValueError("Number sould be between 5 to 10")