student = "Student Name: Samiksha\nCourse: CSE\nCity: Coimbatore\nCollege: XYZ College"

file = open("students.txt", "w")
file.write(student)
file.close()

print("Student details saved successfully")
