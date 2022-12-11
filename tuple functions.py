text = 'Python'

text_tuple = tuple(text)
print("Tuple: ", text_tuple)
print("Lnegth of list: ", len(text_tuple))
print("Count of 'P' in tuple: ", text_tuple.count('P'))
print("Index of 'y' in tuple: ", text_tuple.index('y'))

tuple_ = (5, 2, 24, 3, 1, 6, 7)  
sorted_ = tuple(sorted(tuple_))  
print("Tuple after sortings: ", sorted_)

print("Minimum element in tuple: ", min(tuple_,))
print("Maximum element in tuple: ", max(tuple_,))

# cmp() doesn't exist in Python 3.0 so we will make a cmp function for this
def cmp(a, b):
    return (a > b) - (a < b) 

tuple1, tuple2 = (123, 'xyz'), (456, 'abc')

print(cmp(tuple1, tuple2))
print(cmp(tuple2, tuple1))

reversed_ = tuple(reversed(tuple_))
print("Tuple after reversing: ", reversed_)