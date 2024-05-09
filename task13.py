
correct_email = "admin@mail.com"
correct_password = "Admin@123"


attempts_left = 3


while attempts_left > 0:
    
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    
    if email == correct_email and password == correct_password:
        print("Login is Successful")
        break
    else:
        attempts_left -= 1
        if attempts_left == 0:
            print("You have been blocked.")
        else:
            print(f"Invalid username or password. {attempts_left} attempts left.")
