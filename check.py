#!/usr/bin/env python

import tornado.web
import hashlib
from sha import sha
from tornado.options import define


define("port", default=8000, type=int, help="run on the given port")

class YibanAuthHandler(tornado.web.RequestHandler):
    def get(self):
        signature = self.get_argument("signature",None)
        timestamp = self.get_argument("timestamp",None)
        nonce = self.get_argument("nonce",None)
        echostr = self.get_argument("echostr",None)
        token = sha("woshijidutu").hexdigest()
        lst = [token,timestamp,nonce]
        lst.sort()
        sha1 = hashlib.sha1()
        map(sha1.update,list)
        hashcode = sha1.hexdigest()
        if hashcode == signature:
            return echostr


    
