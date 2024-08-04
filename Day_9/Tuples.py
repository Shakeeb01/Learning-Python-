# Tuples are ordered collection of data items.They store Multiple items in a single varibale.Tuple
#items seprated by commas and enclosed within round brackets (). Tuples are unchageable mean we can not alter them after creation.
tup = (1,34,434,"shah","green")
# print(tup,type(tup))



# this is how we can update the values of tuples in directly.
Countries = ("Spain","Italy","Pakistan","England","Germany")
temp = list(Countries)  #here i created the temporary list.
temp.append("Russia")  # then append the new data in list.
temp.pop(3) 
temp[2] = "Finland"
Countries = tuple(temp)
print(Countries)


#We can concatenate two tuples
country1 = ("Pakistan","Finland")
country2 = ("Luxembourg","Italy")
Europe = country1+country2
print(Europe)