# Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40
# Prompt user to input student marks
marks = int(input("Enter the student's marks (between 0 and 100): "))

if marks > 79:
    grade = "A"
elif 60 <= marks <= 79:
    grade = "B"
elif 50 <= marks <= 59:
    grade = "C"
elif 40 <= marks <= 49:
    grade = "D"
else:
    grade = "E"

print(f"The student's grade is: {grade}")
