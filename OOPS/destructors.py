#destructors-are called when an object gets destroyed
#syntax
# def __del__(self):
# 	body of destructor

class Employee:
	def __init__(self):
		print("Employee created.")
	def __del__(self):
		print("Destructor called,Employee deleted.")
obj=Employee()
del obj


#destructor is called after the program ended


print("\n")
class Employee2: 
  
    # Initializing  
    def __init__(self): 
        print('Employee created') 
  
    # Calling destructor 
    def __del__(self): 
        print("Destructor called") 
  
def Create_obj(): 
    print('Making Object...') 
    obj = Employee2() 
    print('function end...') 
    return obj 
  
print('Calling Create_obj() function...') 
obj = Create_obj() 
print('Program End...') 


print("\n")
# Python program to illustrate destructor 
  
class A: 
    def __init__(self, bb): 
        self.b = bb 
  
class B: 
    def __init__(self): 
        self.a = A(self) 
    def __del__(self): 
        print("die") 
  
def fun(): 
    b = B() 
  
fun() 
