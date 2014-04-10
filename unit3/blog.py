import os
import webapp2
import jinja2
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)
    
######### Pags and Styles
class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))



######### Main
class MainPageBlog(Handler):
	def get(self):
		#posts = db.GqlQuery("SELECT * FROM Blog ORDER BY created DESC LIMIT 10")

		#Alternative
		posts = Blog.all().order('-created')
		#for post in posts:
			#print vars(post)
		#self.render("index.html", posts = posts)
		self.render("front.html", posts = posts)



######## Blog Class
class Blog(db.Model):
	subject = db.StringProperty(required = True)
	content = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)

	def render(self):
		self._render_text = self.content.replace('\n', '<br>')
		return render_str("post.html", post = self) #We're receiving the post object and we're sending to post.html

######## Post
class MainPagePost(Handler):
	def get(self, error="", subject="", content=""):
		self.render("newpost.html", error=error, subject=subject, content=content)

	def post(self):
		subject = self.request.get('subject')
		content = self.request.get('content')

		if subject and content:
			a = Blog(subject=subject, content=content)
			a.put()
			self.redirect('/unit3/blog/' + str(a.key().id())) # Redirect to de Main Page
		else:
			error = "You need to complete the field"
			self.get(error, subject, content) # Mandamos Mensaje de error

class PermanentLinkPost(Handler):
	def get(self, post_id):
		key = db.Key.from_path('Blog', int(post_id))
		post = db.get(key)

		if not post:
			self.error(404)
			return
		self.render('permant_link.html', post = post)

#app = webapp2.WSGIApplication([('/', MainPageBlog)], debug=True)