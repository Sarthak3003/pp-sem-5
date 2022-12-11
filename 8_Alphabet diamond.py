rows = int(input("Enter number of rows: "))

for i in range(rows,1,-1):
    for space in range(i): 
        print(' ', end="")
    for j in range(i,rows+1):
        print(chr(j+64),end=" ")
    print("")

for i in range(1, rows+1):
    for space in range(i): 
        print(' ', end="")
    for j in range(i,rows+1):
        print(chr(j+64),end=" ")
    print("")
