# # Basic syntax:-

# # before lambda 
# def double(x):
#     return x * 3
# # print(double(2))

# # After lambda
# double = lambda x:x*2
# # print(double(4))


# # ******* Map *********

# # the map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements.


# def double(x):
#     return x * 2
    
# l = [2,3,4,5]
# newL = list(map(double,l))  # map function takes two arguments. first is a function then a iterable.
# # print(newL)


# #********* Filter *********

# # the filter function filters  a sequence of elements based on a given condition.

# def filter_Func(a):
#     return a > 2

# filter_List = list(filter(filter_Func,l))

# print(filter_List)


# ******* reduce ******
# We have to import reduce function to use it .

from functools import reduce

numbers = [1,2,3,4]

def mysum(x,y):
    return x+y
sum = reduce(mysum,numbers)

print(sum)