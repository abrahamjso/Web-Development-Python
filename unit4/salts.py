import random
import string
import hashlib

# implement the function make_salt() that returns a string of 5 random
# letters use python's random module.
# Note: The string package might be useful here.

def make_salt(size=5, chars=string.letters):#+string.digits):
    return "".join(random.choice(chars) for x in range(size))

# implement the function make_pw_hash(name, pw) that returns a hashed password 
# of the format: 
# HASH(name + pw + salt),salt
# use sha256

def make_pw_hash(name, pw):
    salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)

# Implement the function valid_pw() that returns True if a user's password 
# matches its hash. You will need to modify make_pw_hash.

def valid_pw(name, pw, h):
	HASH, salt = h.split(',')
	compare = hashlib.sha256(name+pw+salt).hexdigest()
	if HASH == compare:
		return True
	

h = make_pw_hash('spez', 'hunter2')
print valid_pw('spez', 'hunter2', h)

