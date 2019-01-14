class X(object):
	def __init__(self,a):
		self.num=a
	def doubleup(self):
		self.num*=2
class Y(X):
	def __init__(self,a):
		X.__init__(self,a)
	def tripleup(self):
		self.num*=3
obj=Y(4)
print(obj.num) #4
obj.doubleup()
print(obj.num) # 8
obj.tripleup()
print(obj.num) #24



class person(object):
	def __init__(self,name):
		self.name=name
	def getname(self):
		return self.name
	def isemployee(self):
		return False

class employee(person):
	def __init__(self,name,eid):
		super().__init__(name)
		self.empID=eid
	def isemployee(self):
		return True
	def getID(self):
		return self.empID
emp=employee("person1","E101")
print(emp.getname(),emp.isemployee(),emp.getID())