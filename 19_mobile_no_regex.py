import re

def is_valid_mobile_number(number):
  # Compile the regular expression
  pattern = re.compile(r"^[7-9][0-9]{9}$")
  
  # Use the `search` method to search for a match
  # in the given string
  match = pattern.search(number)
  
  # If the match is not `None`, the number is valid
  if match:
    return True
  else:
    return False

# Test the function
print(is_valid_mobile_number("12897834567890"))  # False
print(is_valid_mobile_number("9865432100"))  # True
