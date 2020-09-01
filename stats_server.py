import tornado.ioloop
import tornado.web
import json
import time
import requests
from pymongo import MongoClient

client = MongoClient(HIDDEN)
db = client['for_project']

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        times = []
        online_total = []
        online_pc = []
        online_mobile = []
        for record in db['stats'].find():
            times.append(record['time'])
            online_total.append(record['online'])
            online_pc.append(record['online_pc'])
            online_mobile.append(record['online_mobile'])
        self.render('stats.html', times=times, online_total=online_total, online_pc=online_pc, online_mobile=online_mobile)

settings = [
    (r"/", MainHandler),
]

app = tornado.web.Application(settings, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()
