Num1 = int(input("Enter Your First Number : "))
Num2 = int(input("Enter Your Second Number : "))
Operator = input("Enter Your Operator :[+,-,*,/] ")

if Operator == "+":
    print(Num1+Num2)
elif Operator == "-":
    print(Num1-Num2)
elif Operator == "*":
    print(Num1*Num2)
elif Operator == "/":
    print(Num1/Num2)
else:
    print("Please Add the valid details.")                