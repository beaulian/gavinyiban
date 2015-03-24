import sae
import tornado.wsgi
from check import YibanAuthHandler
app = tornado.wsgi.WSGIApplication([
		(r"/check",YibanAuthHandler)
	])
application = sae.create_wsgi_app(app)