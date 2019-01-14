#csv module -how to read ,parse,and write csv files  -values are comma separated in these files
import csv
'''
#not change dir if in the same dir
with open('names.csv','r') as csv_file:  
	csv_reader=csv.reader(csv_file)
	#print(csv_reader)
	next(csv_reader) #print from next line skipping first line of heading

	for line in csv_reader:
		print(line)
		#print(line[2]) #show only email 0-first name 1-last name
'''
'''
#for writing in new file  the //copying the csv file
with open('names.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	with open('new_names.csv','w') as new_file:
		csv_writer = csv.writer(new_file, delimiter='\t') #not as csv it is separated by - may take \t / ] - _ etc.

		for line in csv_reader:
			csv_writer.writerow(line)   #task completed new_names generated in same directory but not good for data separation
'''

'''
#now reading this new file
with open('new_names.csv','r') as csv_file:
	csv_reader=csv.reader(csv_file,delimiter='\t') #if delimiter not taken then whole line will taken as one part

	for line in csv_reader:
		print(line)

'''
'''
#now using dict reader and writer  dict-dictionary
with open('names.csv', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	for line in csv_reader:
		#print(line)   #all lines are shown as dictionary with keys given in first line
		print(line['email']) #only emails are shown
'''

#now writing to file using dect writer
with open('names.csv', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	with open('new_names.csv','w') as new_file:
		fieldnames = ['first_name','last_name','email']
		csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames,delimiter='\t')
		csv_writer.writeheader()  # for writing header in first line
		for line in csv_reader:
			csv_writer.writerow(line)


'''
with open('names.csv', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	with open('new_names.csv','w') as new_file:
		fieldnames = ['first_name','last_name']
		csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames,delimiter='\t')
		csv_writer.writeheader()  # for writing header in first line
		for line in csv_reader:
			del line['email']  #to delete email column from the file directly
			csv_writer.writerow(line)

'''

