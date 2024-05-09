# Write a program which accepts email as form input or from terminal.
# Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.
email = input('enter your email? ')
if email.count('@')==1 and len(email)>=4:
    em= email.split('@')[1]
    em.count('.')==1
    print(email + ' is valid')
else:
    print(email +' is invalid')
