import tornado.ioloop
import tornado.web
import json
import time
import requests
from pymongo import MongoClient

client = MongoClient('mongodb://Yanis:1337@ds163679.mlab.com:63679/for_project')
db = client['for_project']
user_id=input("Введите ваш ID ")
user_id=int(user_id)
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        times = []
        online_pc = []
        online_mobile = []
        for record in db['data'].find({'id':user_id}).sort("time"):
            times.append(record['time'])
            if record['online_mobile']==0 and record['online']==1:
                online_pc.append(1)
            else:
                online_pc.append(0)
            if record['online_mobile']==1:
                online_mobile.append(1)
            else:
                online_mobile.append(0)
        self.render('single_table_list1.html', times=times, online=online_pc, online_mobile=online_mobile)

settings = [
    (r"/", MainHandler),
]

app = tornado.web.Application(settings, debug=True)
app.listen(8880)
tornado.ioloop.IOLoop.current().start()