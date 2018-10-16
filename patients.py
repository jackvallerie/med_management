"""
This is the patients module
"""

from flask import make_response, abort
import medications

# create the patients list
PATIENTS = {}


"""
This function responds to a request for /api/patients 
with the complete list of patients

returns: json string of list of patients
"""
def read_all():

    return [PATIENTS[key] for key in sorted(PATIENTS.keys())]


"""
This funciton creates a new patient based on the passed
in patient data

param patient: patient to create in patient structure
returns: 201 on success, 406 on person exists
"""
def create(patient):

    lname = patient.get("lname", None)
    fname = patient.get("fname", None)
    medications = patient.get("medications", None)

    if not patient_exists(lname):
        PATIENTS[lname] = {
            "lname": lname,
            "fname": fname,
            "medications": medications,
        }
        return patient_created_response(fname, lname)
    else:
        patient_already_exists_error(lname)


"""
This function assigns a medication from the available medications 
list to a paitent.

param lname: Last name of patient
param medname: Name of medication to add
returns: 201 on success, 406 on patient doesn't exist or medication
doesn't exist
"""
def assign_medication(lname, medname):
    if patient_exists(lname):
        if medications.medication_exists(medname):
            PATIENTS[lname]["medications"].append(medname)
            return medication_added_response(lname, medname)
        else:
            medications.medication_doesnt_exist_error(medname)
    else:
        patient_doesnt_exist_error(lname)


"""
This function unassogns a medication from a patient.

param lname: Last name of patient
param medname: Name of medication to remove
returns: 201 on success, 406 on patient doesn't exist or patient
doesn't use medication
"""
def delete_medication(lname, medname):
    
    if patient_exists(lname):
        if patient_uses_medication(lname, medname):
            PATIENTS[lname]["medications"].remove(medname)
            return medication_removed_response(lname, medname)
        else:
            patient_doesnt_use_medication_error(lname, medname)
    else:
        patient_doesnt_exist_error(lname)





###################
# helper functions
###################


def patient_exists(lname):
    return lname in PATIENTS and lname is not None

def patient_uses_medication(lname, medname):
    return medname in PATIENTS[lname]["medications"]

def patient_created_response(fname, lname):
    return make_response("{fname} {lname} successfully created".format(
        fname=fname, lname=lname), 201)

def medication_added_response(lname, medname):
    return make_response(
                "{medname} successfully added to {fname} {lname}'s medication list".format(
                    medname=medname,
                    fname=PATIENTS[lname]["fname"],
                    lname=lname))

def medication_removed_response(lname, medname):
    return make_response(
                "{medname} successfully removed from {fname} {lname}'s medication list".format(
                    medname=medname,
                    fname=PATIENTS[lname]["fname"],
                    lname=lname))

def patient_already_exists_error(lname):
    abort(406, "Patient with last name {lname} already exists".format(lname=lname))

def patient_doesnt_exist_error(lname):
    abort(406, "Patient with last name {lname} does not exist".format(lname=lname))

def patient_doesnt_use_medication_error(lname, medname):
    abort(406, "Patient {fname} {lname} does not use {medname}".format(
                    medname=medname,
                    fname=PATIENTS[lname]["fname"],
                    lname=lname))
