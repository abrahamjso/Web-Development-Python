import webapp2 

import unit2, unit2.hw
#from unit2.validations import *
from unit2.form import *
from unit2.hw.rot13 import *
from unit2.hw.signup import *

class MainPage(webapp2.RequestHandler):

	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write('Hello Udacity')


application = webapp2.WSGIApplication([('/', MainPage),

										('/unit2/form', FormHandler),
										('/unit2/thanks', ThanksHandler),	

										('/unit2/hw/rot13', Unit2Rot13Handler),
										('/unit2/hw/signup', SignupHandler),
										('/unit2/hw/welcome', WelcomeHandler)
									], debug = True ) 

