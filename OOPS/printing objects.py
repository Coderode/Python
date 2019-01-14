#printing objects
#it gives us information about objects we are working with
class test:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def __repr__(self):
		return "Test a:%s b:%s" %(self.a,self.b)
	def __str__(self):
		return "From str method of Test: a is %s," \
		       "b is %s" %(self.a,self.b)
#driver code
t=test(1234,5678)
print(t) #this calls __str__()
print([t]) #this calls __repr__()

#if no __str__ method is defined print(t) uses __repr__
#if no __repr__ method is defined then the default is used
