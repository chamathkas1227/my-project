print("Hello, World!")
print("This is the second file of project 2 branch")

#modification
# Get the student's score from user input
score = float(input("Enter the student's score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"The student's grade is: {grade}")
