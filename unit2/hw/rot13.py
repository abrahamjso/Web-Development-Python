import webapp2 

form = """
<h2>Enter some text to ROT13</h2>
<form method="post">
	<textarea rows="8" cols="35" name="text" value="">%s</textarea>
	<br>
	<input type="submit">
</form>

"""

class Unit2Rot13Handler(webapp2.RequestHandler):
	
	def write_form(self, tx_input = ''):
		self.response.out.write(form %tx_input)


	def get(self):
		#self.response.out.write(form)
		self.write_form()

	def post(self):
		tx_input = self.request.get("text")
		tx_input = rot13(tx_input)
		self.write_form(tx_input)

def rot13(tx_input):
	return tx_input.encode('rot13')

print rot13("hola")