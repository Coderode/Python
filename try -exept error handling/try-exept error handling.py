'''
we give error name by us using try and except 
'''
'''
try:
	f=open('testfile.txt') #show error if file not exist  given in except part  #not existing file
	var=bad_var  #it is also an error 

except FileNotFoundError:   #noly for error related if file not exist
	print('sorry.this file does not exist.')
except Exception:  #for all errors
	print('something went wrong')
'''
try:
	f=open('test_file.txt') #existing file
	# var=bad_var
	f=open('currupt_file.txt') #existing file (if have to raise exception  with error message)
	if f.name=='currupt_file.txt':
		raise Exception

#if error do this
except FileNotFoundError as e:
	print(e)  #error show itself
except Exception as e:
	# print(e)
	print('Error!')

#if no error do this
else:  
	print(f.read())  
	f.close()

#this runs even if there is error or not
finally:
	print("executing finally...")
