

# Input four numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))


largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3
if num4 > largest:
    largest = num4

print("The largest number is:", largest)
