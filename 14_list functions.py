import random

text = 'Python'

text_list = list(text)
print("List: ", text_list)
print("Lnegth of list: ", len(text_list))
print("Count of 'P' in list: ", text_list.count('P'))
print("Index of 'y' in list: ", text_list.index('y'))

text_list.append('s')
print("List after appending: ", text_list)

text_list.insert(0, 'A ')
print("List after inserting: ", text_list)

list_2 = [1,2,3]
text_list.extend(list_2)
print("List after extending: ",text_list)

text_list.remove('A ')
print("List after removing: ", text_list)

text_list.pop()
print("List after poping: ", text_list)

text_list.reverse()
print("List after reversing: ", text_list)

num_list = []
for i in range(0, 10):
    num_list.append(random.randint(0,10))
num_list.sort()
print("List after sorting: ", num_list)

text_list_2 = text_list.copy()
print("List after copying: ", text_list_2)

text_list_2 = text_list.clear()
print("List after clearing: ", text_list_2)