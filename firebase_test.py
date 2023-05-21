import firebase_admin
from firebase_admin import credentials

import firebase_admin # 파이어 베이스 패키지
from firebase_admin import credentials # 파이어 베이스 패키지
from firebase_admin import firestore # 파이어 베이스 패키지
import matplotlib.pyplot as plt # matlab관련 패키지
from pandas.core.indexes import interval 
from matplotlib.animation import FuncAnimation # 그래프 실시간 애니메이션을 위한 패키지
import schedule
import time

cred=credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)


db=firestore.client() # 파이어 베이스 객체 생성
doc_ref_s=db.collection(u'sound') # Collection이 sound인 레퍼런스 생성

copy_time=[]
copy_val_s=[]
dtime=[]
val_s=[]


def animate():
    docs_s=doc_ref_s.stream() # 스트림 생성
  
    # sound데이터 뽑아 오기
    for doc in docs_s:
        data=doc.to_dict()
        data=dict(sorted(data.items())) # 정렬
        dtime=list(data.keys()) # 시각 추출
        val_s=list(data.values()) # 데이터 추출
        print(data, val_s)
        
    copy_time=list(range(len(dtime)))
    print("copytime",copy_time)
    # plt.cla()
    # plt.plot(copy_time,val_s,label='sound') # 그래프 라벨 이름 설정
    # plt.legend(loc='upper left') # legend 위치 조정
    # plt.tight_layout()


schedule.every(5).seconds.do(animate)
while True:
    schedule.run_pending()
    time.sleep(1)
# ani=FuncAnimation(plt.gcf(),animate,interval=1000) # 1초마다 그래프 업데이트
# plt.tight_layout()
# plt.show()
# plt.savefig("graph.png")