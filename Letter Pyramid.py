import math

# n = int(input("Enter number of rows: "))
# for i in range (65,(65+n)):
#     # inner loop for jth columns
#     for space in range(n-i): 
#         print(' ',end=' ')
#     for j in range(65,i+1):
#         print(chr(j),end="")
        
#     print()


rows=5
# outer loop for ith row
for i in range (1,rows+1):
    asciichr = 65
    for space in range(math.floor(rows-i/2)): 
       print(' ',end=' ')
    # inner loop for jth columns
    for j in range(1, i):
        char = chr(asciichr)
        print(char+' ' ,end="")
        asciichr += 1

    print()