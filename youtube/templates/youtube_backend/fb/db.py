import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials. Certificatie('firebase-sdk.json')

firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection('').document('')