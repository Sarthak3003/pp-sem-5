########################### Break ###########################

while True:
       age = int(input("Please enter your age:"))
       if age >= 18:
              break
       else:
             print("You’re not eligible to vote")


########################### Continue ###########################
for letter in 'Python ': 
    if letter == ' ': 
        continue 
    print ('Letters: ', letter)


########################### Pass ###########################
for letter in 'Programming': 
    if letter == 'x': 
        pass 
    print ('Letters: ', letter)