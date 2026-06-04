import json

# 6.1 SAVE TO A TEXT FILE

report = "Patient Name: Samiksha\nIssue: Fever\nStatus: Admitted"

with open("report.txt", "w") as file:
    file.write(report)

print("Report saved to report.txt")


# 6.2 READ ALL REPORTS FROM FILE

with open("report.txt", "r") as file:
    content = file.read()

print("\nContents of report.txt:")
print(content)


# 6.3 SAVE AS JSON

patient = {
    "patient_name": "Samiksha",
    "patient_id": 1001,
    "department": "Cardiology",
    "status": "Admitted"
}

with open("patient.json", "w") as file:
    json.dump(patient, file, indent=4)

print("\nPatient data saved to patient.json")


# 6.4 LOAD FROM JSON

with open("patient.json", "r") as file:
    loaded_patient = json.load(file)

print("\nLoaded JSON Data:")
print(loaded_patient)
