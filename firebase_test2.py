import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred=credentials.Certificate('key.json')
ref=db.reference('sound')
print(ref.get())