#str() vs repr()
s='hello ,world'
print(str(s))
print(str(2.0/11.0))

print(repr(s))
print(str(2.0/11.0))
#str()-is used for creating output for end user(readable)
#repr()-mainly used for debugging and development(unambiguous)

import datetime
today=datetime.datetime.now()
print(str(today))#-prints readable format 
print(repr(today)) #prints-official format


print("\n")

#in classes
class Complex: 
  
    # Constructor 
    def __init__(self, real, imag): 
       self.real = real 
       self.imag = imag 
  
    # For call to repr(). Prints object's information 
    def __repr__(self): 
       return 'Rational(%s, %s)' % (self.real, self.imag)     
  
    # For call to str(). Prints readable form 
    def __str__(self): 
       return '%s + i%s' % (self.real, self.imag)     
  
  
# Driver program to test above 
t = Complex(10, 20) 
  
print (str(t))  # Same as "print t" 
print (repr(t))
