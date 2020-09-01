import time
import requests
from pymongo import MongoClient
token='Da9b9c19a20120d2b8f573240491af2fc41116ceb9d0eafe5bea70fa2a6277649544b'
client = MongoClient('mongodb://Yanis:1337@ds163679.mlab.com:63679/for_project')
db = client['for_project']
while True:
    for record in db['Registered_users'].find():
        user_id=int(record["id"])
        i=0
        for single in db['data'].find({"id": user_id})[:14]:
            a=single["online_mobile"]
            b=single["online"]
            if a==1 or b==1:
                i=i+1
            print(i)
        if i>=14:
            time.sleep(15*60)