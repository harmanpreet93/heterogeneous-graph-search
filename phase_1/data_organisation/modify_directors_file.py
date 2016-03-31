'''
Create modified directors file from directors.csv with syntax as follow:
Eg: director,<movies director directed>
'''

#!usr/bin/python
import sys
import os

# create file containing only directors
def create_directors_only_file(input_file,output_file):
	print "Please wait, it may take few seconds..."
	lines = input_file.readlines()

	for line in lines:
		arr = line.split(',')
		director = arr[0].lstrip().rstrip() + ' ' + arr[1].lstrip().rstrip() + '\n'
		output_file.write(director)

	output_file.close()
	input_file.close()

# create file containing <director,movie> (jut combining the firstname and lastname into one column)
def create_directors_file_with_full_name_as_first_column(input_file,output_file):
	print "Please wait, it may take few seconds..."
	lines = input_file.readlines()

	for line in lines:
		arr = line.split(',')
		director = arr[0].lstrip().rstrip() + ' ' + arr[1].lstrip().rstrip() + ','
		movie = arr[2].lstrip().rstrip() + '\n'
		output_file.write(director+movie)

	output_file.close()
	input_file.close()

def create_directors_hashmap(input_file):
	directors_hashmap = {}
	print "Please wait, it may take few seconds to create directors_hashmap..."
	lines = input_file.readlines()

	for line in lines:
		arr = line.split(',')
		director = arr[0].lstrip().rstrip() + ' ' + arr[1].lstrip().rstrip()
		movie = arr[2].lstrip().rstrip()
		if directors_hashmap.has_key(director):
			directors_hashmap[director].append(movie)
		else:
			list_of_movie = list()
			list_of_movie.append(movie)
			directors_hashmap[director] = list_of_movie
		
	input_file.close()
	print 'directors_hashmap created'
	return directors_hashmap

def create_modified_directors_file(directors_hashmap,output_file):
	print "Please wait, it may take few seconds to wtite to output file..."

	for key in directors_hashmap:
		# print key,',',directors_hashmap[key]
		line =  ""
		line += key + ','
		for x in range(0,len(directors_hashmap[key])-1):
			line += directors_hashmap[key][x] + ','
		line += directors_hashmap[key][-1] + '\n'
		output_file.write(line)

	print output_file, ' created!'
	output_file.close()


if __name__ == '__main__':

	if len(sys.argv) < 3:
		sys.exit("Usage: python fileName.py directors.csv modified_directors.csv")

	directors_file = open(sys.argv[1],'r')
	modified_file = open(sys.argv[2],'w')
	
	# create_directors_only_file(directors_file,modified_file)

	# directors_hashmap = create_directors_hashmap(directors_file)

	# create_modified_directors_file(directors_hashmap,modified_file)

	create_directors_file_with_full_name_as_first_column(directors_file,modified_file)
