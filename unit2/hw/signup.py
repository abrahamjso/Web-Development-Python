import webapp2
import re

############ Constant ###########

FORM = """
<!DOCTYPE html>
<html>
    <head>
    <title>Sign Up</title>
    <style type="text/css">
        label {text-align: right}
        #error {color: red}
    </style>
    </head>
    <body>
        <h2> Register User </h2>

        <form method="post">
            <label>Username</label>
            <input type="text" name="username" value="%(username)s"><span id="error">%(error_user)s</span>
            <br>

            <label>Password</label>
            <input type="password" name="password" value="%(password)s"><span id="error">%(error_pass)s</span>
            <br>

            <label>Verify Password</label>
            <input type="password" name="verify" value="%(verify)s"><span id="error">%(error_val_pass)s</span>
            <br>

            <label>Email (Optional)</label>
            <input type="text" name="email" value="%(email)s"><span id="error">%(error_email)s</span>
            <br>

            <input type="submit">
        </form>
    </body>
</html>
"""

FORM_UDACITY = """

<!DOCTYPE html>

<html>
  <head>
    <title>Sign Up</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

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
          %(error_user)s  
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
            %(error_pass)s
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
            %(error_val_pass)s
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
            %(error_email)s
          </td>
        </tr>
      </table>

      <input type="submit">
    </form>
  </body>

</html>
"""

WELCOME = """
<!DOCTYPE html>
<html>
    <head>
        <title>Unit 2 Signup</title>
    </head>

    <body>
        <h2>Welcome, %(username)s!</h2>
    </body>
</html>
"""
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")


############ verifys ###########
def valid_username(username):
    return USER_RE.match(username)

def valid_password(password):
    return PASS_RE.match(password)

def valid_email(email):
    return EMAIL_RE.match(email)

########### Signup #################
class SignupHandler(webapp2.RequestHandler):
    def write_form(self, username="", password="", verify="", email="",
                    error_user='', error_pass='', error_val_pass='', error_email=''):
        self.response.out.write(FORM %{ 'username': username,
                                        'password': password,
                                        'verify': verify,
                                        'email': email,

                                        'error_user': error_user,
                                        'error_pass': error_pass,
                                        'error_val_pass': error_val_pass,
                                        'error_email': error_email})

    def get(self):
        self.write_form()

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        validate_pass = self.request.get('verify')
        email = self.request.get('email')

        if not(valid_username(username) and valid_password(password)):
            self.write_form(username, password, validate_pass, email, error_user='That\'s not a valid user', error_pass='That\'s not a valid password' )
        elif(validate_pass != password or not validate_pass):
            self.write_form(username, password, validate_pass, email, error_val_pass='Your pass does not match') 
        elif( email ):
            if not(valid_email(email)):
                self.write_form(username, password, validate_pass, email, error_email="Your email is invalid")
            else:
                self.redirect("/unit2/welcome?username=%s" %username) #Send to welcome in the same path, this probably change the path
        else:
            self.redirect("/unit2/welcome?username=%s" %username) #Send to welcome in the same path, this probably change the path

########### Welcome #################
class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        if not username:
            self.redirect('signup')
        else:
            self.response.write(WELCOME %{'username': username})
