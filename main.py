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
