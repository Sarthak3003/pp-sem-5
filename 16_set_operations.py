## add()
my_set = {1, 2, 3}
# Use add() to add an element to the set
my_set.add(4)
# The set now contains 1, 2, 3, and 4
print(my_set)


## update()
my_set = {1, 2, 3}
# Use update() to add multiple elements to the set
my_set.update([4, 5, 6])
# The set now contains 1, 2, 3, 4, 5, and 6
print(my_set)


##copy()
my_set = {1, 2, 3}
# Use copy() to create a copy of the set
new_set = my_set.copy()
# The new set contains the same elements as the original set
print(new_set)


## union()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Create the union of the two sets using the "|" operator
union_set = set1 | set2 ## or use union() in place of | operator
# The union set contains all the elements from both sets
print(union_set)  # Output: {1, 2, 3, 4, 5}


##intersection()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Create the intersection of the two sets using the "&" operator
intersection_set = set1 & set2 ## or use intersection() in place of & operator
# The intersection set contains only the elements that are present in both sets
print(intersection_set)  # Output: {3}


## difference()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Create the difference of the two sets using the "-" operator
difference_set = set1 - set2 ## or use difference() in place of - operator
# The difference set contains only the elements that are present in set1 but not set2
print(difference_set)  # Output: {1, 2}


