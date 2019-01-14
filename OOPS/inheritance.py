#major advantage of oops is re-use
#a (super class or Base class) is inherited by another class called subclass
#the subclass adds some attributes to superclass
#in python3 class Person is similar to class Person(object)
class Person(object):
	#constructor
	def __init__(self,name):
		self.name=name
	#to get name
	def getName(self):
		return self.name
	#to check if this person is employee
	def isEmployee(self):
		return False

#inherited or subclass (person in bracket)-shows inheritance of Person class
class Employee(Person):
	#here we return true
	def isEmployee(self):
		return True

#driver code
emp=Person("person1")  #obj of person
print(emp.getName(),emp.isEmployee())

emp=Employee("person2") #obj of Employee
print(emp.getName(),emp.isEmployee())




#to check if a class is subclass of another?
#using issubclass() function
class Base(object):
	pass
class Derived(Base):
	pass
#driver code
print(issubclass(Derived,Base)) #true
print(issubclass(Base,Derived))#false

d=Derived()
b=Base()
#b is not an instance of Derived
print(isinstance(b,Derived))
#but d is an instance of base
print(isinstance(d,Base))

#object class-object is root of all classes
#python supports multiple inheritance