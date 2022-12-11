'''
Demonstrate the following Operators in Python with suitable examples.
i) Arithmetic Operators
ii) Relational Operators
iii) Assignment Operator
iv) Logical Operators
v) Bit wise Operators
vi) Ternary Operator
vii) Membership Operators
viii) Identity Operators
'''

########################### Arithmetic Operators (+,-,*,/) ###########################
val1 = 2
val2 = 3
res = val1 + val2
print(res)


########################### Relational Operators (>,<,=) ###########################
a = 9
b = 5
print(a > b)


########################### Assignment Operators (=,+=,-=) ###########################
a = 3
b = 5

a += b
print(a)
a -= b
print(a)


########################### Logical Operators (AND, OR, NOT) ###########################
a = 10
b = 10
c = -10
  
if a > 0 and b > 0:
    print("The numbers are greater than 0")
  
if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
    print("Atleast one number is not greater than 0")


########################### Bitwise operations (&,|,~.^,>>,<<) ###########################
a = 10
b = 4
 
# Print bitwise AND operation
print("a & b =", a & b)
# Print bitwise OR operation
print("a | b =", a | b)
# Print bitwise NOT operation
print("~a =", ~a)
# print bitwise XOR operation
print("a ^ b =", a ^ b)

a = 10
b = -10
 
# print bitwise right shift operator
print("a >> 1 =", a >> 1)
print("b >> 1 =", b >> 1)
a = 5
b = -10
# print bitwise left shift operator
print("a << 1 =", a << 1)
print("b << 1 =", b << 1)


########################### Ternary Operators (if-else) ###########################
a, b = 10, 20

min = a if a < b else b
print(min)


########################### Membership Operators (in, not in) ###########################
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];

if (a in list):
   print("Line 1 - a is available in the given list")
else:
   print("Line 1 - a is not available in the given list")

if (b not in list):
   print("Line 2 - b is not available in the given list")
else:
   print("Line 2 - b is available in the given list")

a = 2
if (a in list):
   print("Line 3 - a is available in the given list")
else:
   print("Line 3 - a is not available in the given list")


########################### Identity Operators (is, is not) ###########################
x = '101'
y = '101'
z = '102'
if (x is y):
  print ('x is y')
else:
  print ('x is not y')
if (x is z):
  print('x is z')
else:
  print ('x is not z')
if (y is z):
  print('y is z')
else:
  print ('y is not z')