#The __init__method
#it is similar to constructors in c++
#it is run as soon as an object of a class is instantiated
#useful to do any initialization you want to do with your object
class Person:
	#init method or constructor
	def __init__(self,name='None'):  #using bydefault name as none if not given during calling then it would result none
		self.name=name
	#any method
	#method-member function
	def fun1(self):
		print('Hello, my name is ',self.name)
#using class
p=Person('sandeep')  #name as initial parameter of the class
p.fun1()
print(Person().fun1())