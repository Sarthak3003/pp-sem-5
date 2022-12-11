import math

rows= int(input("Enter number of rows brother: "))
# outer loop for ith row
for i in range (0,rows+1):
    if i == 0:
        continue
    asciichr = 65
    for space in range(rows-i+1): 
       print(' ',end=' ')

    # inner loop for jth columns
    for j in range(1, i+1):
        char = chr(asciichr)
        print(char+' ' ,end=" ")
        asciichr += 1

    print()