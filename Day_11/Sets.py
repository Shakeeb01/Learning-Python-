# Sets are unordered collection of data items.they store multiple items in a single variable.Set items are
# seprated by commas and enclossed  within curly brackets {} .sets are unchangeable.Sets do not contain duplicate values.

s = {2,4,6,2}  # in this set 2 is duplicat so it will print only once.
# print(s)

s1 = {} # empty set has dictionary data type.
# print(type(s1))



# *********  Set Methods ***********


set1 = {1,3,5,6}
set2 = {8,7,3,2,4}
print(set1.union(set2))  # this will add the two sets.

my_set = {2,344,545}

# Add a single element
my_set.add(4)
# Add multiple elements
my_set.update([5, 6])
# Remove a specific element; raises KeyError if element is not found
my_set.remove(2)
# Remove a specific element; does nothing if element is not found
my_set.discard(3)
# Remove and return an arbitrary element; raises KeyError if set is empty
element = my_set.pop()
# Remove all elements
my_set.clear()
# Check if all elements of set1 are in set2
is_subset = set1.issubset(set2)

# Check if all elements of set2 are in set1
is_superset = set1.issuperset(set2)

# Check if set1 and set2 have no elements in common
is_disjoint = set1.isdisjoint(set2)

# Create a copy of a set
set_copy = set1.copy()