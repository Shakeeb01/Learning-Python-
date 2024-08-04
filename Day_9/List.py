#Introduction to List
# List are ordered collection of data items.
#They store multiple items in a single variable.
#List can store different types of data types.


# Basic Syntax :-
Numbers = [2,343,5535353,4334]
Colors = ["red","green","balck","blue","Orange","pink"]
# Accessing the Value of any list by passing specific index.
# Numbers[4]

#this is how we check wether the element is present in this list or not.

# if "Yellow" in Colors:
#     print("Yellow is Present")
# else:
#     print("Yellow is not present")
#this is how we conver negative index into positive index
Colors[-3] 
# print(Colors[len(Colors)-3])  # => this line will subtract the negative index from the total length then the remaining index will be executed.




# ******************* List Comprehension *********************
#List comprehension are used to for creating new list from other iterables like list,tuples etc.
# Basic Syntax :
# [(expression) for item in (iterable) if (condition)]




# 1. Simple List Comprehension: Generating a list of squares of numbers from 0 to 9.
squares = [x**2 for x in range(9)]
print(squares)

# 2. List Comprehension with Condition: 
EvenNumbers = [i for i in range(20) if i % 2 == 0]
print(EvenNumbers)

OddNums = [n for n in range(10) if n % 2 != 0]
print(OddNums)

# 3. List Comprehension with Function
def double(x):
    return x * 2

doubled = [double(x) for x in range(1,10)]
print(doubled)   