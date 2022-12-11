# open both files
'''
Isse phele bana lena dono files bhai
'''
with open('first.txt','r') as firstfile, open('second.txt','a') as secondfile:
    for line in firstfile:
        secondfile.write(line)