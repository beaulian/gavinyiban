import sae
import tornado.wsgi
from check import YibanAuthHandler

settings = {
	"debug":True
}

app = tornado.wsgi.WSGIApplication([
		(r"/check",YibanAuthHandler),**settings
	])
application = sae.create_wsgi_app(app)