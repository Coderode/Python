#polymorphism - having many forms
#same function name (but diff signatures)
#being uses for diff types
#inbuilt polymorphic functions
print(len("Sandeep")) #len() being used for string
print(len([1, 4, 6]))  #len() being used for list


#user defined polymorphic functions
def add(x,y,z=0):
	return x+y+z

print(add(2,3))
print(add(2,3,4))




print("\n")
#polymorphism with class methods
class India():
	def capital(self):
		print("New delhi is capital of india.")
	def language(self):
		print("Hindi the primary language of india.")
	def type(self):
		print("India is a developing country.")
class USA():
	def capital(self):
		print("Washington ,d.c. is the capital of USA.")
	def language(self):
		print("English is the primary language in USA.")
	def type(self):
		print("USA is a developed country.")
obj_ind=India()
obj_usa=USA()
for country in (obj_ind,obj_usa):
	country.capital()
	country.language()
	country.type()



print("\n")
#polymorphism with inheritance
#process of reimplementing a method in the child class is kn/as method overriding
class Bird:
	def intro(self):
		print("There are many types of birds.")
	def flight(self):
		print("Most of the birds can fly but some cannot.")
class sparrow(Bird):
	def flight(self):
		print("Sparrows can fly.")
class ostrich(Bird):
	def flight(self):
		print("Ostriches cannot fly.")
obj_bird=Bird()
obj_spr=sparrow()
obj_ost=ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()






print("\n")
#polymorphism with a function and objects
#a function that can take any object
#taking above exmaple of india and usa classes
def func(obj):
	obj.capital()
	obj.language()
	obj.type()
obj_ind=India()
obj_usa=USA()

func(obj_ind)
func(obj_usa)