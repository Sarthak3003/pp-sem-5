##Zero division 
try:
    x = 1 / 0
except ZeroDivisionError:
    print("You cannot divide a number by zero!")

##Value Error
try:
    x = int("hello")
except ValueError:
    print("Invalid input! Please provide an integer.")


##TypeError
try:
    x = "hello" + 5
except TypeError:
    print("Invalid operation! You cannot concatenate a string and an integer.")

##NameError
try:
    print(x)
except NameError:
    print("Unknown variable! Please make sure the variable has been defined.")


##indexerror
try:
    x = [1, 2, 3]
    print(x[3])
except IndexError:
    print("Invalid index! Please provide an index that is within the range of the sequence.")
