import time
from pymongo import MongoClient
import json, requests
while True:
    try:
        client = MongoClient(HIDDEN)
        db = client['for_project']
        request1 = "https://api.vk.com/method/groups.getMembers?group_id=62351504&v=5.23&count=1000&fields=online,online_mobile"
        f=time.strftime("%Y-%m-%d %H:%M:%S")

        request_data=requests.get(request1)
        json_data = json.loads(request_data.text)

        data = []


        online_total = 0
        online_mobile_total=0


        for user in json_data['response']['items']:
            online_mobile = 0
            if 'online_mobile' in user.keys():
                online_mobile = user['online_mobile']

            online_mobile_total += online_mobile
            online_total += user['online']

            data_elem = {"id": user['id'], "online": user['online'], "online_mobile": online_mobile, "time": f}
            data.append(data_elem)

        db['data'].insert(data)
        print(time)
        print(online_mobile_total, online_total)
        stats={"time": f ,"online": online_total, "online_mobile":online_mobile_total, "online_pc":(online_total-online_mobile_total), "ammount": json_data['response']['count']}
        db['stats'].insert_one(stats)
        time.sleep(15*60)
    except:
        time.sleep(60)
