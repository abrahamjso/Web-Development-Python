import webapp2 

form = """

<!DOCTYPE html>

<html>
  <head>
    <title>Sign Up</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>
  <body>
    <h2>Signup</h2>
    <form method="post">
      <table>
        <tr>
          <td class="label">
            Username
          </td>
          <td>
            <input type="text" name="username" value="%(username)s">
          </td>
          <td class="error">
            
          </td>
        </tr>

        <tr>
          <td class="label">
            Password
          </td>
          <td>
            <input type="password" name="password" value="%(password)s">
          </td>
          <td class="error">
            
          </td>
        </tr>

        <tr>
          <td class="label">
            Verify Password
          </td>
          <td>
            <input type="password" name="verify" value="%(verify)s">
          </td>
          <td class="error">
            
          </td>
        </tr>

        <tr>
          <td class="label">
            Email (optional)
          </td>
          <td>
            <input type="text" name="email" value="%(email)s">
          </td>
          <td class="error">
            
          </td>
        </tr>
      </table>

      <input type="submit">
    </form>
  </body>

</html>
"""

class SignupHandler(webapp2.RequestHandler):
	def write_form(self, username='', password='', verify='', email=''):
		self.response.out.write(form % {'username': username,
                                    'password': password,
                                    'verify': verify,
                                    'email': email})

	def get(self):
		self.write_form()

	def post(self):
		username = self.request.get('username')
		password =  self.request.get('password')
		pass_verify = self.request.get('verify')
		email = self.request.get('email')

		#if not(username and password and pass_verify):
