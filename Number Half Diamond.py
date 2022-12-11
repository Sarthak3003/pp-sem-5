rows = int(input("Enter number of rows: "))

#uppar ka traingle
for i in range(rows+1):
    for j in range(rows-i,rows+1):
        print(j,end='')
    print("\t")

#neeche ka triangle
for i in range(0, rows):
    for j in range(i+1,rows+1):
        print(j,end='')
    print("\t")