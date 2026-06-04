def create_student(name, course, city, college):
    student = {
        "name": name,
        "course": course,
        "city": city,
        "college": college
    }
    return student

my_student = create_student("Samiksha", "CSE", "Coimbatore", "XYZ College")
print(my_student)
