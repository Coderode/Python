#class and instance variables or attributes
#class variables are variables whose value is assigned in class
#class variables-value assigned in class declaration
#instance variables-inside methods and constructors
class CSStudent:
	#class variable
	stream='cse'
	def __init__(self,roll):
		#instance variable
		self.roll=roll
	def setAddress(self,address):
		#inst. var.
		self.address=address
	def getAddress(self):
		return self.address


#objects
a=CSStudent(101)
b=CSStudent(102)
print(a.stream)#-cse
print(b.stream)#-cse
print(a.roll) #101
#class variable can be accessed using class name

print(CSStudent.stream)#-cse

a.setAddress("Noida, Up")
print(a.getAddress()) 

print(a.stream)
print(b.stream)
a.stream="ece"  #only object variable changes-creates instance variable for the object
print(a.stream)
print(b.stream)
CSStudent.stream="mec"  #here class variable changes
print(a.stream)
print(b.stream)



'''
#an empty class
class Test:
	pass
'''