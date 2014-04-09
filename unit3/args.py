def foo(a, *args):
	print "a value:", a
	print "....."
	for arg in args:
		print arg

def calculate_sum(*args):
	return sum(args)

def ignore_firstargs_calculate_sum(a, *iargs):
	requiered_sum = calculate_sum(*iargs)
	print "sum is: ", requiered_sum

#ignore_firstargs_calculate_sum(1,3,3,3)

def fun(a, **kwargs):
	print 'a is:', a
	print 'other values kwargs...'
	print 'b is', kwargs['b']
	print 'c is', kwargs['c']

d = {'b': 5, 'c': 3}

#fun(1,b=3,d=8)

class Model(object):
	def __init__(self, name):
		self.name= name

	def save(self, force_update=False, force_insert=False):
		if force_update and force_insert:
			raise ValueError("Cannot perform both operations")
		if force_update:
			print "Updated an existing record"
		if force_insert:
			print "Created a new record"

class ChildModel(Model):
	def save(self, *args, **kwargs):
			if self.name=='abcd':
				super(ChildModel, self).save(*args, **kwargs)
			else:
				None

c=ChildModel('abcd')
c.save(force_insert=True)