# Implement a program that takes 3 form inputs or from the terminal,
# and stores them in three variables. Return the largest of the three. 
# Do this without using the the inbuilt max () function!
v1= int(input('enter value one? '))
v2= int(input('enter value two? '))
v3= int(input('enter value three? '))
if v1>v2 and v1>v3:
    print(str(v1) +' is greater')
elif v2>v1 and v2>v3:
    print(str(v2) +' is greater')
else:
    print(str(v3) + ' is greater')


