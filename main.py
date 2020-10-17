import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials


cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection('employee').document('empdoc')

doc_ref.set({
    'name': 'Parwiz',
    'lname': 'Forogh',
    'age': 24
})










emp_ref = db.collection('employee')
docs = emp_ref.stream()

for doc in docs:
    print('{} => {} '.format(doc.id, doc.to_dict()))

