# Take 10 numbers from the user and save them to a file
# numbers = []
# for i in range(10):
#   number = input(f"Enter number {i+1}: ")
#   numbers.append(number)

# with open("t1.txt", "w") as f:
#   for number in numbers:
#     f.write(f"{number}\n")

# # Read the contents of the file, sort the data, and save it to a different file
# with open("t1.txt", "r") as f:
#   numbers = [int(x) for x in f.read().split()]

# numbers.sort()

# with open("t2.txt", "w") as f:
#   for number in numbers:
#     f.write(f"{number}\n")


## part 2
import re

# Read the contents of the file
with open("textfile.txt", "r") as f:
  data = f.read()

# Compile the regular expressions
name_regex = re.compile(r"^(Mr|Ms|Mrs)\.[\s\w]+")
website_regex = re.compile(r"(https?://)?(www\.)?(\w+\.\w+)")
email_regex = re.compile(r"\w+@\w+\.\w+")
phone_regex = re.compile(r"\d{3}[-*]\d{3}[-*]\d{2,4}")

# Find the names of the users
names = name_regex.findall(data)
print("Names of the users:")
print(names)

# Find the website names excluding http/s
websites = website_regex.findall(data)
print("\nWebsite names excluding http/s:")
print(websites)

# Find the email IDs
emails = email_regex.findall(data)
print("\nEmail IDs:")
print(emails)

# Find the phone numbers
phones = phone_regex.findall(data)
print("\nPhone numbers:")
print(phones)
