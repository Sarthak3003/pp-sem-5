def tower_of_hanoi(n, source, destination, auxiliary):
  if n == 1:
    print(f"Move disk 1 from {source} to {destination}")
    return

  tower_of_hanoi(n-1, source, auxiliary, destination)
  print(f"Move disk {n} from {source} to {destination}")
  tower_of_hanoi(n-1, auxiliary, destination, source)

# Test the function
tower_of_hanoi(3, "A", "B", "C")

## lambda function wala q
greater = lambda x, y: x if x > y else y

print(greater(3, 5))  # 5
print(greater(10, 4)) # 10