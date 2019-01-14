#automate parsing and renaming of multiple files
#to arrange files in preferend arrangement as files needed may be any file if we have 1000 of files 
#file names are as before arranging
'''
Mars - Our solar system - #5.txt
Mercury - Our solar system - #2.txt
Neptune - Our solar system - #8.txt
Pluto - Our solar system - #10.txt
Saturn - Our solar system - #7.txt
The sun - Our solar system - #1.txt
Uranus - Our solar system - #9.txt
Venus - Our solar system - #3.txt
'''

import os
os.chdir('/Users/hp/Desktop/python/Demos')   #change the directory of python to directory of files
#print(os.getcwd()) #checking for directory
for f in os.listdir():
	
	#print(f) #prints all fils in the folder
	#print(os.path.splitext(f))  #splits file names and the extension as tuple
	f_name, f_ext = os.path.splitext(f)  #saves file names in variable file_name so on
	#print(f_name)
	#print(f_name.split('-')) #split file names also where the - is and make as list
	f_title,f_course,f_num=f_name.split('-') #puts all three parts of file_name in these three sections 
	#print(f_title)

	f_title=f_title.strip()  #removing other extra spaces using this
	f_course=f_course.strip()
	f_num=f_num.strip()[1:].zfill(2) #removed hash here from f_num numbering with 2 digits

	#print('{}-{}-{}{}'.format(f_num,f_course,f_title,f_ext)) #changing format here of names as f_course is same in all
	#print('{}-{}{}'.format(f_num,f_title,f_ext)) #now the names has been set in proper way so take it as variable
	new_name='{}-{}{}'.format(f_num,f_title,f_ext)
	os.rename(f,new_name) #renaming every f in the folder  #now work has done
	
	#print(f)
#after renaming 	

'''
01-The sun.txt
02-Mercury.txt
03-Venus.txt
04-Earth.txt
05-Mars.txt
06-Jupiter.txt
07-Saturn.txt
08-Neptune.txt
09-Uranus.txt
10-Pluto.txt
'''



