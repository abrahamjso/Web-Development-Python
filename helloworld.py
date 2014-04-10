import webapp2 

import unit2, unit2.hw
#from unit2.validations import *
from unit2.form import *
from unit2.hw.rot13 import *
from unit2.hw.signup import *

from unit3.blog import *

class MainPage(webapp2.RequestHandler):

	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write('Hello Udacity\n\n')
		visits = self.request.cookies.get('visits', '0')

		if visits.isdigit():
			visits = int(visits) + 1
		else:
			visits = 0

		self.response.headers.add_header('Set-Cookie', 'visits=%s,val=3,val2=ab' % (visits) )
		self.response.out.write('You are the visitor number %s' %visits)


application = webapp2.WSGIApplication([('/', MainPage),

										('/unit2/form', FormHandler),
										('/unit2/thanks', ThanksHandler),	

										('/unit2/hw/rot13', Unit2Rot13Handler),
										('/unit2/signup', SignupHandler),
										('/unit2/welcome', WelcomeHandler),

										('/unit3/blog', MainPageBlog),
										('/unit3/blog/([0-9]+)', PermanentLinkPost),
										('/unit3/blog/newpost', MainPagePost)

									], debug = True ) 

