#a simple class
class test:  
	def fun(self):  #method self-compulsary in every method
	#it is fun without any input parameter
	#we don't give value for this self parameter
	#similar to this pointer in c++ and this reference in java
	#if we call myobj.method(arg1,arg2)-class.method(myobj,arg1,arg2)-this all the special self is about

		print('Hello')
#driver code
obj=test()  #creating object
obj.fun()  #accessing method from class


