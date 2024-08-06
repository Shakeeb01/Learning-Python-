my_dict = {
    "name" : "shakeeb",
    "Age":22,
    "Profession":"Backend Developer",
}
print(my_dict)
print(my_dict["Age"])  # This is how we can access single value of our dictionary.

for key in my_dict.keys():
    print(my_dict[key])
    

print(my_dict.values())     # this is to get values of dictionary
   
   
   
   
   # *************** Dictionary Methods ************
   
   
ep1 = {
    1:45,
    2:60,
    3:56,
    4:90
}

ep2 = {
    5:85,
    6:10,
    7:96,
}

ep1.pop(4) # this will remove one value .
ep1.popitem() # this will remove last key  value pair .
ep2.clear() # this will remove all the values from the dictionary.
print(ep2)
ep1.update(ep2)   # this will add the values of one dictionary to another.
print(ep1)
   