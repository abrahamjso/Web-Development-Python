import hashlib, hmac

def hash_str(s):
    return hashlib.md5(s).hexdigest()

def make_secure_val(s):
    return "%s,%s" % (s, hash_str(s))

# -----------------
# User Instructions
# 
# Implement the function check_secure_val, which takes a string of the format 
# s,HASH
# and returns s if hash_str(s) == HASH, otherwise None 

def check_secure_val(h):
    s, HASH = h.split(',')
    if HASH == hash_str(s):
        return s
    
    #Alternative
	#val = h.split('|')[0]
	#if h == make_secure_val(val):
	#	return val

#x = make_secure_val('5')
#print x
#print check_secure_val(x)

# Implement the hash_str function to use HMAC and our SECRET instead of md5
SECRET = 'imsosecret'
def hash_str(s):
	val = hmac.new(SECRET, s).hexdigest()
	print val
    ###Your code here

hash_str('Abraham')