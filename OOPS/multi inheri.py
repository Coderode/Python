#multiple inheritance
#specify all parent classes as comma separated
class Base1(object):
	def __init__(self):
		self.str1="hello1"
		print("base1")
class Base2(object):
	def __init__(self):
		self.str2="hello2"
		print("Base2")
class Derived(Base1,Base2):
	def __init__(self):
		#calling constructors of base1 and base2 classes
		Base1.__init__(self)
		Base2.__init__(self)
		print("Derived")
	def printStrs(self):
		print(self.str1,self.str2)

ob=Derived() #as we create an object it runs __init__ method by its own
#this line prints
#base1
#base2
#Derived
ob.printStrs() #str1 and str2 are come in derived when we called init function of base classed in derived class
#it prints
#hello1 hello2
ob.__init__()#-> base1 base2 Derived





print("\n")
'''access parent members in a subclass '''
#using parent class name
class Base(object):
	def __init__(self,x):
		self.x=x
class Derived2(Base):
	def __init__(self,x,y):
		Base.x=x #parent member
		self.y=y
	def printXY(self):
		print(Base.x,self.y)
		#print(self.x,self.y)#wil also work

#driver code
d=Derived2(10,20)
d.printXY() #->prints 10 20





print("\n")
#using super()
class Base3(object):
	def __init__(self,x):
		self.x=x
class Derived3(Base):
	def __init__(self,x,y):
		#super(Derived3,self).__init__(x) or 
		super().__init__(x)
		self.y=y
	def printXY(self):
		print(self.x,self.y)

#driver code
d=Derived3(10,20)
d.printXY()