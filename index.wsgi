import sae
import tornado.wsgi
import tornado.web
import hashlib
from sha import sha
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

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
        map(sha1.update,lst)
        hashcode = sha1.hexdigest()
        if hashcode == signature:
            self.write(echostr)
    

    def post(self):
        str_xml = self.request.body
        xml = etree.fromstring(str_xml)
        Content=xml.find("Content").text
        msgType=xml.find("MsgType").text
        createTime=xml.find("CreateTime").text
        fromUser=xml.find("FromUserName").text
        toUser=xml.find("ToUserName").text
        self.write('''<xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName> 
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[%s]]></Content>
                </xml>''' % (toUser,fromUser,createTime,content))


settings = {
	"debug":True
}

app = tornado.wsgi.WSGIApplication([
		(r"/check",YibanAuthHandler)],**settings)
application = sae.create_wsgi_app(app)