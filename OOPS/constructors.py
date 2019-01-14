#constructor-for instantiating an object 
#to initialize to the data members of the class when an object of class is created
#types-1.default constructor-which doesnot accept any argument (self is used)
#2.parameterized constructor-which have parameters (with self)


#default constructor
class Person:
	p=""
	def __init__(self):
		self.p="person1"
	def print_person(self):
		print(self.p)

obj=Person()
obj.print_person()


print("\n")
#parameterized constructor
class Addition:
	first=0
	second=0
	answer=0
	def __init__(self,f,s):
		self.first=f
		self.second=s
	def display(self):
		print("First number = ",self.first) 
		print("Second number = ",self.second)
		print("Addition of two numbers = ",self.answer)
	def calculate(self):
		self.answer = self.first + self.second 

obj=Addition(1000,2000)
obj.calculate()
obj.display()