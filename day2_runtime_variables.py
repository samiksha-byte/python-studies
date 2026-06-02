# Gmail Registration

def get_gmail_details():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter New Email ID: ")
    recovery_email = input("Enter Recovery Email ID: ")

    print_gmail_details(name, phone, email, recovery_email)

def print_gmail_details(name, phone, email, recovery_email):
    print("\n----- Gmail Registration -----")
    print("Name:", name)
    print("Phone:", phone)
    print("Email:", email)
    print("Recovery Email:", recovery_email)


# Aadhaar Registration

def get_aadhaar_details():
    name = input("Enter Name: ")
    dob = input("Enter Date of Birth: ")
    gender = input("Enter Gender: ")
    mobile = input("Enter Mobile Number: ")
    address = input("Enter Address: ")

    print_aadhaar_details(name, dob, gender, mobile, address)

def print_aadhaar_details(name, dob, gender, mobile, address):
    print("\n----- Aadhaar Registration -----")
    print("Name:", name)
    print("DOB:", dob)
    print("Gender:", gender)
    print("Mobile:", mobile)
    print("Address:", address)


# College Admission

def get_college_details():
    application_id = input("Enter Application ID: ")
    student_name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    department = input("Enter Department: ")
    marks = input("Enter Mark Percentage: ")

    print_college_details(application_id, student_name, course, department, marks)

def print_college_details(application_id, student_name, course, department, marks):
    print("\n----- College Admission -----")
    print("Application ID:", application_id)
    print("Student Name:", student_name)
    print("Course:", course)
    print("Department:", department)
    print("Marks:", marks)


# Flight Booking

def get_flight_details():
    passenger_name = input("Enter Passenger Name: ")
    source = input("Enter Source City: ")
    destination = input("Enter Destination City: ")
    travel_date = input("Enter Travel Date: ")

    print_flight_details(passenger_name, source, destination, travel_date)

def print_flight_details(passenger_name, source, destination, travel_date):
    print("\n----- Flight Booking -----")
    print("Passenger Name:", passenger_name)
    print("Source:", source)
    print("Destination:", destination)
    print("Travel Date:", travel_date)


# Hospital Registration

def get_hospital_details():
    patient_name = input("Enter Patient Name: ")
    age = input("Enter Age: ")
    doctor_name = input("Enter Doctor Name: ")
    problem = input("Enter Health Issue: ")

    print_hospital_details(patient_name, age, doctor_name, problem)

def print_hospital_details(patient_name, age, doctor_name, problem):
    print("\n----- Hospital Registration -----")
    print("Patient Name:", patient_name)
    print("Age:", age)
    print("Doctor Name:", doctor_name)
    print("Health Issue:", problem)


# Function Calls

get_gmail_details()
get_aadhaar_details()
get_college_details()
get_flight_details()
get_hospital_details()
