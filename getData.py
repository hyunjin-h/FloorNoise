import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def getData():
    cred=credentials.Certificate('key.json')

    firebase_admin.initialize_app(cred,{
        'databaseURL' : 'https://capstone-116d0-default-rtdb.firebaseio.com/'
    })
    ref = db.reference('sound')
    print(ref.get())
    return ref.get()
