# Write a program input a password.
# Give them only 4 attempts to check the passwords entered against “admin@123”. 
# If the password is correct access is granted. After you show them a message , the account is blocked.
# Number of attempts allowed
attempts_left = 4


password = "admin@123"


while attempts_left > 0:
    
    user_password = input("Enter the password: ")

    
    if user_password == password:
        print("Access granted.")
        break
    else:
        attempts_left -= 1
        if attempts_left == 0:
            print("Account blocked.")
        else:
            print(f"Incorrect password. {attempts_left} attempts left.")

