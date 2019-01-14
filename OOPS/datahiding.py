#data hiding and object printing
#in python we use __(double underscore) before the attributes (data or method)
#name and those attributes will not be directly visible outside
class Myclass:
	#hidden member of class
	__hiddenvariable=0  #like making private data in c++

	#a member method that changes __hiddenvariable
	def add(self,increment):
		self.__hiddenvariable+=increment
		print(self.__hiddenvariable)

#driver code
myobj=Myclass()
myobj.add(2)
myobj.add(5)


#this line causes error
# print(Myclass.__hiddenvariable) #error-Myclss has no attribute __hiddenvariable
# print(myobj.__hiddenvariable)   #it is like private data in class in c++

#hidden variables can't be used ouside the class using object

#but can be accessed using trick
#nothing in python is truly private
myobj2=Myclass()
print(myobj2._Myclass__hiddenvariable)
print(myobj._Myclass__hiddenvariable)