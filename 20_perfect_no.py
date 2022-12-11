def perfect(n):
      # Compute the sum of the factors of n, other than n itself
  sum = 0
  for i in range(1, n):
    if n % i == 0:
      sum += i

  # Return True if the sum equals n, and False otherwise
  return sum == n

# Test the function
print(perfect(6))   # True
print(perfect(28))  # True
print(perfect(29))  # False

