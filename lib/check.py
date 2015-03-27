#!/usr/bin/env python
#-*- coding:utf-8 
import time
import tornado.web
import hashlib
from lxml import etree


class YibanAuthHandler(tornado.web.RequestHandler):
    def get(self):
        signature = self.get_argument("signature",None)
        echostr = self.get_argument("echostr",None)
        timestamp = self.get_argument("timestamp",None)
        nonce = self.get_argument("nonce",None)
        token = "woshijidutu"
        lst = [token,timestamp,nonce]
        lst.sort()
        sha1 = hashlib.sha1()
        map(sha1.update,lst)
        hashcode = sha1.hexdigest()
        if hashcode == signature:
            self.write(echostr)

    def post(self):
        str_xml = self.request.body
        xml = etree.fromstring(str_xml)
        fromUser=xml.find("FromUserName").text  
        toUser=xml.find("ToUserName").text
        msgType=xml.find("MsgType").text
        createTime=xml.find("CreateTime").text
        content=xml.find("Content").text
        self.set_header("Content-Type","application/xml")
        self.render("yiban.xml",ToUser=fromUser,FromUser=toUser,CreateTime=int(time.time()),Content="我是加文,欢迎关注continue技术小组!")
        

    
