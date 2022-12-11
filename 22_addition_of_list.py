# Define the two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Use the `map` function to add the elements of the two lists
result = list(map(lambda x, y: x+y, list1, list2))

# Print the result
print(result)  # [5, 7, 9]

##cube of odd numbers in two lists
# Define the input list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Use the `filter` function to get only the odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# Use the `map` function to compute the cubes of the odd numbers
cubes = list(map(lambda x: x**3, odd_numbers))

# Print the result
print(cubes)  # [1, 27, 125, 343]
