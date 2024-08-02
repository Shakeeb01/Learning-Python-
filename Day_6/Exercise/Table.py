# this is python programm which will take the number for multiplication from user and also the length of the table.
Num = int(input("Enter your number for multiplication table."))
Length = int(input("What should be the length of table ? "))
for i in range(1,Length+1,1):
    print(Num,"X",i,"=",i*Num)