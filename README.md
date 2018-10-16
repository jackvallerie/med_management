# **Medication Management**

This is a RESTful API built with Flask and [Connexion](https://connexion.readthedocs.io/en/latest/index.html#) that allows the user to perform the following: 

- Add a new medication to the list of available medications
- Create a new patient
- Assign a patient a new medication from the list of available medications
- Remove a medication from the list of medications assigned to a patient

Connexion is set up such that the API is described using the OpenAPI 2.0
Specification (this is in the swagger.yml file), and those endpoints are mapped to
Python functions (these are split between the patients.py and medications.py
modules).


To use the API, first clone the Git repository:
```
git clone https://github.com/jackvallerie/med_management.git
```

then cd into the directory and install the dependencies (in a virtual 
environment, if you'd like):
```
pip install -r requirements.txt
```

To run the server:
```
python server.py
```

The server will run on http://localhost:5000 by default.  To see the Swagger 
API interface, go to http://localhost:5000/api/ui and click **medications** and
**patients** to see the operations associated with each module.  You can
interact with the API from this UI by filling in the parameter fields for
requests that require it, then clicking the 'Try it out!' button at the
bottom left of that operation box.

The patient and medication lists are set to empty lists in their respective
modules.