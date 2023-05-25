import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

cred=credentials.Certificate('key.json')

firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://capstone-116d0-default-rtdb.firebaseio.com/'
})
ref = db.reference('soundData')
data=ref.get()
# JSON 문자열로 변환
json_string = json.dumps(data)

# JSON 문자열 파싱
parsed_data = json.loads(json_string)

# 두 번째 값들 추출
values = list(parsed_data.values())
second_values = [int(value) for value in values]

print(second_values)