from datetime import datetime

dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
dob = datetime.strptime(dob_input, "%Y-%m-%d")

today = datetime.today()
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))


if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
    months = today.month + (12 - dob.month) - 1
else:
    months = today.month - dob.month

days = (today - datetime(today.year, today.month, 1)).days

print(f"Age: {age} years, {months} months, {days} days")
