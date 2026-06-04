# CREATE — One Patient Record as a Dictionary

patient = {
    "patient_name": "Arun",
    "patient_id": 1001,
    "department": "Cardiology",
    "details": {
        "age": 45,
        "blood_group": "O+",
        "weight": 72
    }
}

print("Patient Record Created:", patient)


# READ — Access Specific Fields

print("Patient Name:", patient["patient_name"])
print("Blood Group:", patient["details"]["blood_group"])


# UPDATE AND DELETE

patient["details"]["weight"] = 75
print("Updated Weight:", patient["details"]["weight"])

del patient["department"]
print("After Deletion:", patient)


# LIST OF DICTIONARIES — Multiple Patient Records

patients = [
    {"patient_name": "Arun", "patient_id": 1001, "details": {"age": 45, "blood_group": "O+"}},
    {"patient_name": "Meena", "patient_id": 1002, "details": {"age": 32, "blood_group": "A+"}},
    {"patient_name": "Karthik", "patient_id": 1003, "details": {"age": 28, "blood_group": "B+"}}
]

for p in patients:
    print(p["patient_name"], "→ Blood Group:", p["details"]["blood_group"])


# FUNCTION THAT CREATES A PATIENT RECORD

def create_patient(patient_name, patient_id, age, blood_group):
    return {
        "patient_name": patient_name,
        "patient_id": patient_id,
        "details": {
            "age": age,
            "blood_group": blood_group
        }
    }

new_patient = create_patient("Arun", 1001, 45, "O+")
print("Generated Patient Record:", new_patient)
