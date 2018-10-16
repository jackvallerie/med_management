"""
This is the medications module
"""

from flask import make_response, abort
import patients

# create the medications list
MEDICATIONS = []


"""
This function responds to a request for /api/medications
with the complete list of medications

returns: json string of list of medications
"""
def read_all():

    return sorted(MEDICATIONS)


"""
This function adds a new medication to the medications list

param medname: name of medication to add
returns: 201 on success, 406 on medication exists
"""
def create(medname):

    if not medication_exists(medname):
        MEDICATIONS.append(medname)
        return medication_added(medname)
    else:
        medication_already_exists_error(medname)



###################
# helper funcitons
###################

def medication_added(medname):
    return make_response(
        "{medname} successfully added to medications list".format(medname=medname))

def medication_exists(medname):
    return medname in MEDICATIONS and medname is not None

def medication_already_exists_error(medname):
    abort(
        406, "Medication {medname} already exists".format(medname=medname))

def medication_doesnt_exist_error(medname):
    abort(
        406, 
        "Medication {medname} does not exist in the medicatons list".format(medname=medname))