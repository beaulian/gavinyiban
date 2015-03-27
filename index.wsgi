import sae
import os.path
import tornado.wsgi
from check import YibanAuthHandler
settings = {
    "debug":True
}
handlers = [(r"/check",YibanAuthHandler)]
template_path=os.path.join(os.path.dirname(__file__), "templates")
app = tornado.wsgi.WSGIApplication(handlers=handlers,template_path=template_path,**settings)
application = sae.create_wsgi_app(app)
