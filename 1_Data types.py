'''
Demonstrate about fundamental Data types in Python Programming. (i.e., int, float, complex, bool and string types)
'''

#int type
a = 5
print("Type of a: ", type(a))

#float type
b = 5.0
print("\nType of b: ", type(b))

#complex type
c = 2 + 4j
print("\nType of c: ", type(c))

# Boolean type
d = True
print("\nType of d: ", type(d))

#string type
e = "Python OP"
print("\nType of e: ", type(e))


'''
Demonstrate the working of following functions in Python. i) id( ) ii) type( ) iii) range( )
'''

#id()
x = ('apple', 'banana', 'cherry')
print(id(x))

#type()
print(type(x))

#range()
for i in range(len(x)):
    print(x[i])